from flask import Flask, render_template, request
import os
import traceback
import threading
import logging
from datetime import datetime

# ==========================================================
# APPLICATION INITIALIZATION
# ==========================================================

app = Flask(__name__)
app.config["TEMPLATES_AUTO_RELOAD"] = True

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s"
)

logger = logging.getLogger("WebDragonAI")

# ==========================================================
# SAFE IMPORTS – CORE SERVICES
# ==========================================================

LalKitabEngine = None
log_user_action = None
learn_from_user = None
get_courses_data = None
get_marketing_data = None
update_serp_data = None

try:
    import services.kundali_engine.kundali_engine as kundali_module
    LalKitabEngine = getattr(kundali_module, "LalKitabEngine", None)
    logger.info("LalKitabEngine loaded successfully")
except Exception as e:
    logger.error(f"Engine import failed: {e}")

try:
    from services.user_logger.user_logger import log_user_action
    from services.learning_engine.learning_engine import learn_from_user
except Exception:
    logger.warning("Tracking services unavailable")

try:
    from services.course_data import get_courses_data
    from services.marketing_data import get_marketing_data
except Exception:
    logger.warning("Course / marketing services unavailable")

try:
    from services.serp_worker import update_serp_data
except Exception:
    logger.warning("SERP worker unavailable")

# ==========================================================
# BACKGROUND WORKER
# ==========================================================

def start_serp_worker():

    if update_serp_data is None:
        return

    try:
        thread = threading.Thread(
            target=update_serp_data,
            daemon=True
        )
        thread.start()

        logger.info("SERP Worker Running")

    except Exception:
        logger.error("SERP Worker Failed")
        traceback.print_exc()


if not app.debug:
    start_serp_worker()

# ==========================================================
# DEFAULT SAFE STRUCTURE
# ==========================================================

def build_default_kundali():

    return {
        "personality_summary": "Analysis not generated yet.",
        "lagna": "Unknown",
        "planetary_positions": {},
        "yoga_analysis": [],
        "dosha_analysis": [],
        "transit_analysis": "Transit analysis pending.",
        "destiny_score": 5,
        "generated_at": datetime.utcnow().isoformat()
    }

# ==========================================================
# NORMALIZE ENGINE OUTPUT
# ==========================================================

def normalize_engine_output(raw):

    default = build_default_kundali()

    if not isinstance(raw, dict):
        return default

    try:

        birth_chart = raw.get("birth_chart", {})
        interpretation = raw.get("interpretation_layers", {})
        transit_layer = raw.get("current_transit", {})
        meta = raw.get("meta", {})

        # -----------------------------------------
        # Personality Summary
        # -----------------------------------------

        personality = (
            interpretation.get("birth_chart", {})
            .get("personality_summary")
        )

        # -----------------------------------------
        # Lagna
        # -----------------------------------------

        lagna = birth_chart.get("lagna")

        # -----------------------------------------
        # Planetary Positions
        # -----------------------------------------

        planetary_positions = (
            birth_chart.get("planetary_positions", {})
            .get("by_planet", {})
        )

        if not isinstance(planetary_positions, dict):
            planetary_positions = {}

        # -----------------------------------------
        # Yogas
        # -----------------------------------------

        yogas = birth_chart.get("yogas", [])

        if isinstance(yogas, dict):
            yogas = yogas.get("yogas", [])

        # -----------------------------------------
        # Doshas
        # -----------------------------------------

        doshas = birth_chart.get("doshas", [])

        if isinstance(doshas, dict):
            doshas = doshas.get("doshas", [])

        # -----------------------------------------
        # Transit
        # -----------------------------------------

        transit_data = transit_layer.get("planetary_positions")

        if transit_data:
            transit_summary = "Transit data available."
        else:
            transit_summary = "Transit analysis pending."

        # -----------------------------------------
        # Destiny Score
        # -----------------------------------------

        destiny_score = raw.get("final_destiny_score", 5)

        # -----------------------------------------
        # Generated Time
        # -----------------------------------------

        generated_at = meta.get("generated_at") or default["generated_at"]

        # -----------------------------------------
        # Final Structured Output
        # -----------------------------------------

        return {
            "personality_summary": personality or default["personality_summary"],
            "lagna": lagna or default["lagna"],
            "planetary_positions": planetary_positions,
            "yoga_analysis": yogas,
            "dosha_analysis": doshas,
            "transit_analysis": transit_summary,
            "destiny_score": destiny_score,
            "generated_at": generated_at
        }

    except Exception:

        logger.error("Engine normalization failed")
        traceback.print_exc()

        return default

# ==========================================================
# HOME
# ==========================================================

@app.route("/")
def index():

    return render_template("index.html")

# ==========================================================
# ASTROLOGY PAGE
# ==========================================================

@app.route("/astrology")
def astrology():

    if log_user_action and learn_from_user:
        try:
            user_ip = request.remote_addr or "unknown"

            log_user_action(user_ip, "astrology_page_visit")
            learn_from_user(user_ip, "interest", "astrology")

        except Exception:
            logger.warning("Tracking failed")

    return render_template(
        "astrology.html",
        detailed_planetary_interpretation=None
    )

# ==========================================================
# KUNDALI GENERATION ROUTE
# ==========================================================

@app.route("/astrology/kundali", methods=["GET", "POST"])
def kundali_route():

    if request.method == "POST":

        try:

            name = request.form.get("name")
            dob = request.form.get("dob")
            tob = request.form.get("tob")
            place = request.form.get("pob")

            if not all([name, dob, tob, place]):

                logger.warning("Incomplete birth data")

                return render_template(
                    "astrology.html",
                    detailed_planetary_interpretation=build_default_kundali()
                )

            if LalKitabEngine is None:

                logger.error("Kundali engine unavailable")

                return render_template(
                    "astrology.html",
                    detailed_planetary_interpretation=build_default_kundali()
                )

            birth_data = {
                "name": name,
                "date": dob,
                "time": tob,
                "place": place
            }

            try:

                engine = LalKitabEngine(birth_data)
                raw_result = engine.generate_kundali()

                logger.info("Kundali generated successfully")

            except Exception as e:

                logger.error(f"Kundali engine crashed: {e}")
                traceback.print_exc()

                raw_result = {}

            final_result = normalize_engine_output(raw_result)

            return render_template(
                "astrology.html",
                detailed_planetary_interpretation=final_result
            )

        except Exception:

            logger.error("Fatal error in kundali route")
            traceback.print_exc()

            return render_template(
                "astrology.html",
                detailed_planetary_interpretation=build_default_kundali()
            )

    return render_template(
        "astrology.html",
        detailed_planetary_interpretation=None
    )

# ==========================================================
# COURSES PAGE
# ==========================================================

@app.route("/courses")
def courses():

    try:
        data = get_courses_data() if get_courses_data else {}
    except Exception:
        data = {}

    return render_template("courses.html", data=data)

# ==========================================================
# MARKETING PAGE
# ==========================================================

@app.route("/marketing")
def marketing():

    try:
        data = get_marketing_data() if get_marketing_data else {}
    except Exception:
        data = {}

    return render_template("marketing.html", data=data)

# ==========================================================
# APPLICATION ENTRY POINT
# ==========================================================

if __name__ == "__main__":

    port = int(os.environ.get("PORT", 5000))

    logger.info(f"Starting Web Dragon AI on port {port}")

    app.run(
        host="0.0.0.0",
        port=port,
        debug=True
    )