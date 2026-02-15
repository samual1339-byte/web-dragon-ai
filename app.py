from flask import Flask, render_template, request
import threading
import os

# =========================
# APP INIT
# =========================
app = Flask(__name__)

# =========================
# SAFE SERVICE IMPORTS
# =========================
from services.user_logger.user_logger import log_user_action
from services.learning_engine.learning_engine import learn_from_user

from services.kundali_engine.kundali_engine import (
    generate_kundali,
    matchmaking_kundali
)

from services.astrology_data import get_astrology_data
from services.course_data import get_courses_data
from services.marketing_data import get_marketing_data

from services.serp_worker import update_serp_data


# =========================
# AUTONOMOUS SERP WORKER
# =========================
def start_serp_worker():
    t = threading.Thread(target=update_serp_data, daemon=True)
    t.start()

if os.environ.get("WERKZEUG_RUN_MAIN") != "true":
    start_serp_worker()


# =========================
# ROUTES
# =========================

@app.route("/")
def index():
    return render_template("index.html")


# -------- ASTROLOGY HOME --------
@app.route("/astrology")
def astrology():
    user_ip = request.remote_addr or "unknown"

    log_user_action(user_ip, "astrology")
    learn_from_user(user_ip, "interest", "astrology")

    data = get_astrology_data()
    return render_template("astrology.html", data=data)


# -------- KUNDALI --------
@app.route("/astrology/kundali", methods=["GET", "POST"])
def kundali_route():   # UNIQUE endpoint name

    user_ip = request.remote_addr or "unknown"

    log_user_action(user_ip, "kundali")
    learn_from_user(user_ip, "sub_interest", "kundali")

    if request.method == "POST":

        name = request.form.get("name")
        dob = request.form.get("dob")
        tob = request.form.get("tob")
        place = request.form.get("pob")  # matches form field

        try:
            result = generate_kundali(
                name=name,
                dob=dob,
                tob=tob,
                place=place
            )
        except Exception as e:
            result = {"error": str(e)}

        dummy_serp = [
            {
                "title": "Astrological Insight",
                "snippet": f"{name}, your planetary alignment suggests strong growth and leadership qualities."
            }
        ]

        return render_template(
            "kundali_result.html",
            kundali=result if isinstance(result, dict) else {},
            serp=dummy_serp,
            data=result
        )

    # GET request
    return render_template(
        "kundali_result.html",
        kundali={},
        serp=None,
        data=None
    )


# -------- MATCHMAKING --------
@app.route("/astrology/matchmaking")
def matchmaking():
    user_ip = request.remote_addr or "unknown"

    log_user_action(user_ip, "matchmaking")
    learn_from_user(user_ip, "sub_interest", "matchmaking")

    data = matchmaking_kundali()
    return render_template("matchmaking_result.html", data=data)


# -------- COURSES --------
@app.route("/courses")
def courses():
    user_ip = request.remote_addr or "unknown"

    log_user_action(user_ip, "courses")
    learn_from_user(user_ip, "interest", "courses")

    data = get_courses_data()
    return render_template("courses.html", data=data)


# -------- MARKETING --------
@app.route("/marketing")
def marketing():
    user_ip = request.remote_addr or "unknown"

    log_user_action(user_ip, "marketing")
    learn_from_user(user_ip, "interest", "marketing")

    data = get_marketing_data()
    return render_template("marketing.html", data=data)


# =========================
# RUN SERVER
# =========================
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)


