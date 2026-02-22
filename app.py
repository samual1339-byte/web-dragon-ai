from flask import Flask, render_template, request
import os
import traceback
import threading

# =========================
# APP INIT
# =========================
app = Flask(__name__)
app.config["TEMPLATES_AUTO_RELOAD"] = True


# =========================
# IMPORT CORE ENGINE
# =========================
try:
    from services.kundali_engine.lalkitab_autonomous.lalkitab_master import LalKitabMaster
    from services.user_logger.user_logger import log_user_action
    from services.learning_engine.learning_engine import learn_from_user
    from services.astrology_data import get_astrology_data
    from services.course_data import get_courses_data
    from services.marketing_data import get_marketing_data
    from services.serp_worker import update_serp_data
except Exception as e:
    print("CRITICAL IMPORT ERROR:", e)
    raise


# =========================
# BACKGROUND WORKER
# =========================
def start_serp_worker():
    try:
        thread = threading.Thread(target=update_serp_data, daemon=True)
        thread.start()
        print("SERP Worker Running")
    except Exception:
        traceback.print_exc()


if not app.debug:
    start_serp_worker()


# =========================
# ROUTES
# =========================

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/astrology")
def astrology():

    user_ip = request.remote_addr or "unknown"
    log_user_action(user_ip, "astrology")
    learn_from_user(user_ip, "interest", "astrology")

    data = get_astrology_data()
    return render_template("astrology.html", data=data)


# ============================================
# KUNDALI — PURE LAL KITAB BASED INTERPRETATION
# ============================================

@app.route("/astrology/kundali", methods=["GET", "POST"])
def kundali_route():

    if request.method == "POST":

        user_ip = request.remote_addr or "unknown"
        log_user_action(user_ip, "kundali")
        learn_from_user(user_ip, "sub_interest", "kundali")

        name = request.form.get("name")
        dob = request.form.get("dob")
        tob = request.form.get("tob")
        place = request.form.get("pob")

        try:
            # =====================================
            # DIRECT ENGINE INITIALIZATION
            # =====================================
            engine = LalKitabMaster(
                name=name,
                dob=dob,
                tob=tob,
                place=place
            )

            # =====================================
            # STRICT LAL KITAB CALCULATION
            # =====================================
            result = engine.generate_lalkitab_kundali()

            if not isinstance(result, dict):
                raise ValueError("Engine did not return structured dictionary")

        except Exception as e:
            print("KUNDALI ENGINE FAILURE")
            traceback.print_exc()

            result = {
                "planets": {},
                "lagna": None,
                "planetary_insight": {},
                "doshas": [],
                "risk_score": None,
                "risk_level": None,
                "remedies": [],
                "interpretation": f"Lal Kitab interpretation failed: {str(e)}",
                "birth_analysis": {},
                "current_analysis": {}
            }

        return render_template(
            "kundali_result.html",
            kundali=result,
            serp=None
        )

    return render_template(
        "kundali_result.html",
        kundali=None,
        serp=None
    )


@app.route("/courses")
def courses():

    user_ip = request.remote_addr or "unknown"
    log_user_action(user_ip, "courses")
    learn_from_user(user_ip, "interest", "courses")

    data = get_courses_data()
    return render_template("courses.html", data=data)


@app.route("/marketing")
def marketing():

    user_ip = request.remote_addr or "unknown"
    log_user_action(user_ip, "marketing")
    learn_from_user(user_ip, "interest", "marketing")

    data = get_marketing_data()
    return render_template("marketing.html", data=data)


# =========================
# PRODUCTION ENTRY
# =========================
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)