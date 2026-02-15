# ======================================
# BACKEND LOGIC LAYER
# ======================================

from services.kundali_engine import (
    generate_kundali,
    matchmaking_kundali,
    enhance_kundali_result,
    enhance_matchmaking_result
)

from services.astrology_data import get_astrology_data
from services.course_data import get_courses_data
from services.marketing_data import get_marketing_data


# -------- ASTROLOGY --------
def get_astrology_dashboard():
    return get_astrology_data()


def process_kundali(form_data):
    base = generate_kundali(
        form_data["name"],
        form_data["dob"],
        form_data["tob"],
        form_data["place"]
    )
    return enhance_kundali_result(base)


def process_matchmaking():
    base = matchmaking_kundali()
    return enhance_matchmaking_result(base)


# -------- COURSES --------
def get_courses_dashboard():
    return get_courses_data()


# -------- MARKETING --------
def get_marketing_dashboard():
    return get_marketing_data()
