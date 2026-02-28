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

try:
    import services.kundali_engine.kundali_engine as kundali_module
    LalKitabEngine = getattr(kundali_module, "LalKitabEngine", None)

   

except Exception as e:
    logger.critical(f"❌ Failed to import LalKitabEngine: {e}")
    raise e


try:
    from services.user_logger.user_logger import log_user_action
    from services.learning_engine.learning_engine import learn_from_user
    from services.astrology_data import get_astrology_data
    from services.course_data import get_courses_data
    from services.marketing_data import get_marketing_data
    from services.serp_worker import update_serp_data
except Exception as e:
    logger.critical(f"❌ Core service import failed: {e}")
    raise e

# ==========================================================
# 🔥 BACKGROUND WORKER (SERP)
# ==========================================================

def start_serp_worker():
    try:
        thread = threading.Thread(
            target=update_serp_data,
            daemon=True,
            name="SERPWorkerThread"
        )
        thread.start()
        logger.info("✅ SERP Worker Running")
    except Exception:
        logger.error("❌ SERP Worker Failed")
        traceback.print_exc()


if not app.debug:
    start_serp_worker()


# ==========================================================
# 🔥 SAFE DEFAULT KUNDALI STRUCTURE (STRICT TEMPLATE SAFE)
# ==========================================================

def get_safe_kundali_response(error_message=None):
    return {
        "birth_data": {},
        "planets": {},
        "lagna": None,
        "doshas": {},
        "yogas": [],
        "impact_analysis": {},
        "remedies": [],
        "risk_score": None,
        "risk_level": None,
        "interpretation": error_message or "Interpretation unavailable.",
        "generated_at": datetime.utcnow().isoformat()
    }


# ==========================================================
# 🔥 ROUTES
# ==========================================================

@app.route("/")
def index():
    return render_template("index.html")


# ==========================================================
# 🔮 ASTROLOGY PAGE
# ==========================================================

@app.route("/astrology")
def astrology():

    user_ip = request.remote_addr or "unknown"

    try:
        log_user_action(user_ip, "astrology")
        learn_from_user(user_ip, "interest", "astrology")
    except Exception:
        logger.warning("⚠ User tracking failed")

    data = get_astrology_data()
    return render_template("astrology.html", data=data)


# ==========================================================
# 🔮 KUNDALI ROUTE (FULLY STABILIZED)
# ==========================================================
@app.route("/astrology/kundali", methods=["GET", "POST"])
def kundali_route():

    if request.method == "POST":

        user_ip = request.remote_addr or "unknown"

        try:
            log_user_action(user_ip, "kundali")
            learn_from_user(user_ip, "sub_interest", "kundali")
        except Exception:
            logger.warning("⚠ Learning engine failed")

        name = request.form.get("name")
        dob = request.form.get("dob")
        tob = request.form.get("tob")
        place = request.form.get("pob")

        if not all([name, dob, tob, place]):
            logger.warning("⚠ Incomplete Kundali form")
            result = get_safe_kundali_response(
                "Incomplete birth details provided."
            )
            return render_template(
                "kundali_result.html",
                kundali=result,
                serp=None
            )

        try:
            logger.info("🔮 Initializing Lal Kitab Engine")

            birth_data = {
                "name": name,
                "date": dob,
                "time": tob,
                "place": place
            }

            engine = LalKitabEngine(birth_data)

            if not hasattr(engine, "generate_kundali"):
                raise AttributeError("generate_kundali() method not found")

            raw_result = engine.generate_kundali()

            if not isinstance(raw_result, dict):
                raise ValueError("Engine returned invalid structure")

            result = get_safe_kundali_response()
            result.update(raw_result)
            result["generated_at"] = datetime.utcnow().isoformat()

            logger.info("✅ Kundali generation successful")

        except Exception as e:
            logger.error("❌ KUNDALI ENGINE FAILURE")
            traceback.print_exc()

            result = get_safe_kundali_response(
                f"Lal Kitab interpretation failed: {str(e)}"
            )

        # ✅ THIS RETURN WAS MISSING
        return render_template(
            "kundali_result.html",
            kundali=result,
            serp=None
        )

    # ✅ GET request fallback
    return render_template(
        "kundali_result.html",
        kundali=None,
        serp=None
    )
# ==========================================================
# 📚 COURSES
# ==========================================================

@app.route("/courses")
def courses():

    user_ip = request.remote_addr or "unknown"

    try:
        log_user_action(user_ip, "courses")
        learn_from_user(user_ip, "interest", "courses")
    except Exception:
        logger.warning("⚠ Tracking failed for courses")

    data = get_courses_data()
    return render_template("courses.html", data=data)


# ==========================================================
# 📈 MARKETING
# ==========================================================

@app.route("/marketing")
def marketing():

    user_ip = request.remote_addr or "unknown"

    try:
        log_user_action(user_ip, "marketing")
        learn_from_user(user_ip, "interest", "marketing")
    except Exception:
        logger.warning("⚠ Tracking failed for marketing")

    data = get_marketing_data()
    return render_template("marketing.html", data=data)


# ==========================================================
# 🚀 PRODUCTION ENTRY POINT
# ==========================================================

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    logger.info(f"🚀 Starting Web Dragon AI on port {port}")
    app.run(host="0.0.0.0", port=port)