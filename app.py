from flask import Flask, render_template, request
import threading
import os
import traceback

# =========================
# APP INIT
# =========================
app = Flask(__name__)
app.config["TEMPLATES_AUTO_RELOAD"] = True


# =========================
# SAFE IMPORT WRAPPER
# =========================
try:
    from services.user_logger.user_logger import log_user_action
    from services.learning_engine.learning_engine import learn_from_user
    from services.kundali_engine.kundali_engine import generate_kundali, matchmaking_kundali
    from services.astrology_data import get_astrology_data
    from services.course_data import get_courses_data
    from services.marketing_data import get_marketing_data
    from services.serp_worker import update_serp_data
except Exception as e:
    print("IMPORT ERROR:", e)

    def log_user_action(*args, **kwargs): pass
    def learn_from_user(*args, **kwargs): pass
    def generate_kundali(*args, **kwargs): return {}
    def matchmaking_kundali(*args, **kwargs): return {}
    def get_astrology_data(): return {}
    def get_courses_data(): return {}
    def get_marketing_data(): return {}
    def update_serp_data(): pass


# =========================
# BACKGROUND WORKER
# =========================
def start_serp_worker():
    try:
        t = threading.Thread(target=update_serp_data, daemon=True)
        t.start()
        print("SERP Worker Started")
    except Exception as e:
        print("Worker Error:", e)


if not app.debug:
    start_serp_worker()


# =========================
# SAFE KUNDALI DEFAULT STRUCTURE
# =========================
def empty_kundali():
    return {
        "planets": {},
        "lagna": None,
        "planetary_insight": {},
        "doshas": [],
        "risk_score": None,
        "risk_level": None,
        "remedies": [],
        "interpretation": None
    }


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

    data = get_astrology_data() or {}
    return render_template("astrology.html", data=data)


@app.route("/astrology/kundali", methods=["GET", "POST"])
def kundali_route():

    user_ip = request.remote_addr or "unknown"
    log_user_action(user_ip, "kundali")
    learn_from_user(user_ip, "sub_interest", "kundali")

    if request.method == "POST":

        name = request.form.get("name")
        dob = request.form.get("dob")
        tob = request.form.get("tob")
        place = request.form.get("pob")

        try:
            result = generate_kundali(
                name=name,
                dob=dob,
                tob=tob,
                place=place
            )

            if not isinstance(result, dict):
                result = empty_kundali()

        except Exception as e:
            print("KUNDALI ERROR:")
            traceback.print_exc()
            result = empty_kundali()
            result["interpretation"] = f"Error generating kundali: {str(e)}"

        dummy_serp = [{
            "title": "Astrological Insight",
            "snippet": f"{name}, your planetary alignment suggests karmic activation and growth cycles."
        }]

        return render_template(
            "kundali_result.html",
            kundali=result,
            serp=dummy_serp
        )

    return render_template(
        "kundali_result.html",
        kundali=empty_kundali(),
        serp=None
    )


@app.route("/astrology/matchmaking")
def matchmaking():

    user_ip = request.remote_addr or "unknown"
    log_user_action(user_ip, "matchmaking")
    learn_from_user(user_ip, "sub_interest", "matchmaking")

    try:
        data = matchmaking_kundali() or {}
    except Exception as e:
        print("MATCHMAKING ERROR:", e)
        data = {}

    return render_template("matchmaking_result.html", data=data)


@app.route("/courses")
def courses():

    user_ip = request.remote_addr or "unknown"
    log_user_action(user_ip, "courses")
    learn_from_user(user_ip, "interest", "courses")

    data = get_courses_data() or {}
    return render_template("courses.html", data=data)


@app.route("/marketing")
def marketing():

    user_ip = request.remote_addr or "unknown"
    log_user_action(user_ip, "marketing")
    learn_from_user(user_ip, "interest", "marketing")

    data = get_marketing_data() or {}
    return render_template("marketing.html", data=data)


# =========================
# PRODUCTION ENTRY
# =========================
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)