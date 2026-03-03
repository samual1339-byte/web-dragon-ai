from flask import Flask, render_template, request
import os
import traceback
import threading
import logging
from datetime import datetime

# ==========================================================
# 🔥 APPLICATION INITIALIZATION
# ==========================================================

app = Flask(__name__)
app.config["TEMPLATES_AUTO_RELOAD"] = True

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s"
)

logger = logging.getLogger("WebDragonAI")

# ==========================================================
# 🔥 SAFE IMPORTS – CORE SERVICES
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
except Exception as e:
    logger.error(f"Engine import failed: {e}")

try:
    from services.user_logger.user_logger import log_user_action
    from services.learning_engine.learning_engine import learn_from_user
except Exception:
    logger.warning("Tracking services not available.")

try:
    from services.course_data import get_courses_data
    from services.marketing_data import get_marketing_data
except Exception:
    logger.warning("Data services not available.")

try:
    from services.serp_worker import update_serp_data
except Exception:
    logger.warning("SERP worker not available.")

# ==========================================================
# 🔥 BACKGROUND WORKER
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
        logger.info("✅ SERP Worker Running")
    except Exception:
        logger.error("❌ SERP Worker Failed")
        traceback.print_exc()


if not app.debug:
    start_serp_worker()

# ==========================================================
# 🔮 SAFE RESULT STRUCTURE (FIXES ALL UNAVAILABLE ISSUES)
# ==========================================================

def build_default_kundali():
    return {
        "personality_summary": "Analysis not generated yet.",
        "lagna": "Unknown",
        "planetary_positions": [],
        "yoga_analysis": [],
        "dosha_analysis": [],
        "transit_analysis": "Transit analysis pending.",
        "destiny_score": 5,
        "generated_at": datetime.utcnow().isoformat()
    }

def calculate_destiny_score(data):
    score = 0

    if data.get("planetary_positions"):
        score += 2
    if data.get("yoga_analysis"):
        score += 3
    if data.get("transit_analysis"):
        score += 2
    if not data.get("dosha_analysis"):
        score += 3


    return min(score, 10)

def normalize_engine_output(raw):
    default = build_default_kundali()

    if not isinstance(raw, dict):
        return default

    default["personality_summary"] = raw.get("personality_summary") or default["personality_summary"]
    default["lagna"] = raw.get("lagna") or default["lagna"]
    default["planetary_positions"] = raw.get("planetary_positions") or []
    default["yoga_analysis"] = raw.get("yoga_analysis") or []
    default["dosha_analysis"] = raw.get("dosha_analysis") or []
    default["transit_analysis"] = raw.get("transit_analysis") or default["transit_analysis"]

    default["destiny_score"] = calculate_destiny_score(default)

    return default

# ==========================================================
# 🏠 HOME
# ==========================================================

@app.route("/")
def index():
    return render_template("index.html")

# ==========================================================
# 🔮 ASTROLOGY PAGE
# ==========================================================

@app.route("/astrology")
def astrology():

    if log_user_action and learn_from_user:
        try:
            user_ip = request.remote_addr or "unknown"
            log_user_action(user_ip, "astrology_page_visit")
            learn_from_user(user_ip, "interest", "astrology")
        except Exception:
            logger.warning("Tracking failed.")

    return render_template(
        "astrology.html",
        detailed_planetary_interpretation=None
    )

# ==========================================================
# 🔮 KUNDALI ROUTE (FULLY FIXED)
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
                return render_template(
                    "astrology.html",
                    detailed_planetary_interpretation=build_default_kundali()
                )

            if LalKitabEngine is None:
                logger.error("LalKitabEngine missing.")
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
            except Exception as e:
                logger.error(f"Kundali engine crashed: {e}")
                traceback.print_exc()
                raw_result = {}

            final_result = normalize_engine_output(raw_result)

            return render_template(
                "astrology.html",
                detailed_planetary_interpretation=final_result
            )

        except Exception as e:
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
# 📚 COURSES
# ==========================================================

@app.route("/courses")
def courses():
    try:
        data = get_courses_data() if get_courses_data else {}
    except Exception:
        data = {}
    return render_template("courses.html", data=data)

# ==========================================================
# 📈 MARKETING
# ==========================================================

@app.route("/marketing")
def marketing():
    try:
        data = get_marketing_data() if get_marketing_data else {}
    except Exception:
        data = {}
    return render_template("marketing.html", data=data)

# ==========================================================
# 🚀 ENTRY POINT
# ==========================================================

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    logger.info(f"🚀 Starting Web Dragon AI on port {port}")
    app.run(host="0.0.0.0", port=port, debug=True)