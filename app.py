from flask import Flask, render_template

# 1️⃣ CREATE APP FIRST
app = Flask(__name__)

# 2️⃣ IMPORT SERVICES (AFTER app exists)
from services.astrology_data import get_astrology_data
from services.course_data import get_courses_data
from services.marketing_data import get_marketing_data

# ---------------- HOME ----------------
@app.route("/")
def home():
    return render_template("index.html")

# ---------------- ASTROLOGY ----------------
@app.route("/astrology")
def astrology():
    data = get_astrology_data()
    return render_template("astrology.html", results=data)

# ---------------- COURSES ----------------
@app.route("/courses")
def courses():
    data = get_courses_data()
    return render_template("courses.html", results=data)

# ---------------- MARKETING ----------------
@app.route("/marketing")
def marketing():
    data = get_marketing_data()
    return render_template("marketing.html", results=data)

# ---------------- RUN ----------------
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
