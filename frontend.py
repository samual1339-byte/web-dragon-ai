# ======================================
# FRONTEND CONTROLLER
# ======================================

from services.user_logger import log_user_action
from services.learning_engine import learn_from_user

from backend import (
    get_astrology_dashboard,
    process_kundali,
    process_matchmaking,
    get_courses_dashboard,
    get_marketing_dashboard
)


def handle_astrology(user_ip):
    log_user_action(user_ip, "astrology")
    learn_from_user(user_ip, "interest", "astrology")
    return get_astrology_dashboard()


def handle_kundali(user_ip, form_data):
    log_user_action(user_ip, "kundali")
    learn_from_user(user_ip, "sub_interest", "kundali")
    return process_kundali(form_data)


def handle_matchmaking(user_ip):
    log_user_action(user_ip, "matchmaking")
    learn_from_user(user_ip, "sub_interest", "matchmaking")
    return process_matchmaking()


def handle_courses(user_ip):
    log_user_action(user_ip, "courses")
    learn_from_user(user_ip, "interest", "courses")
    return get_courses_dashboard()


def handle_marketing(user_ip):
    log_user_action(user_ip, "marketing")
    learn_from_user(user_ip, "interest", "marketing")
    return get_marketing_dashboard()
