# ==========================================================
# 🧿 KUNDALI MATCHING ENGINE – ASHTA KOOTA CORE (STABLE)
# ==========================================================

import math


# ----------------------------------------------------------
# Constants
# ----------------------------------------------------------

RASHIS = [
    "Aries", "Taurus", "Gemini", "Cancer",
    "Leo", "Virgo", "Libra", "Scorpio",
    "Sagittarius", "Capricorn", "Aquarius", "Pisces"
]

VARNA_MAP = {
    "Aries": "Kshatriya",
    "Taurus": "Vaishya",
    "Gemini": "Shudra",
    "Cancer": "Brahmin",
    "Leo": "Kshatriya",
    "Virgo": "Vaishya",
    "Libra": "Shudra",
    "Scorpio": "Brahmin",
    "Sagittarius": "Kshatriya",
    "Capricorn": "Vaishya",
    "Aquarius": "Shudra",
    "Pisces": "Brahmin"
}

GANA_MAP = {
    "Aries": "Deva",
    "Taurus": "Manushya",
    "Gemini": "Rakshasa",
    "Cancer": "Deva",
    "Leo": "Manushya",
    "Virgo": "Rakshasa",
    "Libra": "Deva",
    "Scorpio": "Manushya",
    "Sagittarius": "Rakshasa",
    "Capricorn": "Deva",
    "Aquarius": "Manushya",
    "Pisces": "Rakshasa"
}

NADI_MAP = {
    "Aries": "Adi",
    "Taurus": "Madhya",
    "Gemini": "Antya",
    "Cancer": "Adi",
    "Leo": "Madhya",
    "Virgo": "Antya",
    "Libra": "Adi",
    "Scorpio": "Madhya",
    "Sagittarius": "Antya",
    "Capricorn": "Adi",
    "Aquarius": "Madhya",
    "Pisces": "Antya"
}

FRIEND_SIGNS = {
    "Aries": ["Leo", "Sagittarius"],
    "Taurus": ["Virgo", "Capricorn"],
    "Gemini": ["Libra", "Aquarius"],
    "Cancer": ["Scorpio", "Pisces"],
    "Leo": ["Aries", "Sagittarius"],
    "Virgo": ["Taurus", "Capricorn"],
    "Libra": ["Gemini", "Aquarius"],
    "Scorpio": ["Cancer", "Pisces"],
    "Sagittarius": ["Aries", "Leo"],
    "Capricorn": ["Taurus", "Virgo"],
    "Aquarius": ["Gemini", "Libra"],
    "Pisces": ["Cancer", "Scorpio"]
}


# ==========================================================
# Internal Utility Functions
# ==========================================================

def _get_moon_sign(planets):
    moon = planets.get("Moon")
    if not moon or "rashi" not in moon:
        raise ValueError("Moon sign missing in chart")
    return moon["rashi"]


def _varna_score(boy_sign, girl_sign):
    return 1 if VARNA_MAP[boy_sign] == VARNA_MAP[girl_sign] else 0


def _vashya_score(boy_sign, girl_sign):
    return 2 if boy_sign == girl_sign else 1


def _tara_score(boy_sign, girl_sign):
    boy_index = RASHIS.index(boy_sign)
    girl_index = RASHIS.index(girl_sign)
    diff = abs(boy_index - girl_index)
    return 3 if diff % 3 != 0 else 0


def _yoni_score(boy_sign, girl_sign):
    return 4 if boy_sign != girl_sign else 2


def _graha_maitri_score(boy_sign, girl_sign):
    if girl_sign in FRIEND_SIGNS.get(boy_sign, []):
        return 5
    return 2


def _gana_score(boy_sign, girl_sign):
    return 6 if GANA_MAP[boy_sign] == GANA_MAP[girl_sign] else 3


def _bhakoot_score(boy_sign, girl_sign):
    boy_index = RASHIS.index(boy_sign)
    girl_index = RASHIS.index(girl_sign)
    diff = abs(boy_index - girl_index)
    if diff in [2, 6, 8]:
        return 0
    return 7


def _nadi_score(boy_sign, girl_sign):
    if NADI_MAP[boy_sign] == NADI_MAP[girl_sign]:
        return 0
    return 8


def _mangal_cross_check(boy_chart, girl_chart):
    mangal_houses = [1, 4, 7, 8, 12]
    boy_mars = boy_chart.get("Mars", {}).get("house")
    girl_mars = girl_chart.get("Mars", {}).get("house")

    boy_mangal = boy_mars in mangal_houses
    girl_mangal = girl_mars in mangal_houses

    if boy_mangal and girl_mangal:
        return "Balanced Mangal Dosha"
    elif boy_mangal or girl_mangal:
        return "Mangal Imbalance"
    return "No Mangal Issue"


# ==========================================================
# 🔥 MAIN MATCH FUNCTION
# ==========================================================

def match_kundalis(boy_chart, girl_chart):

    if not isinstance(boy_chart, dict) or not isinstance(girl_chart, dict):
        raise TypeError("Charts must be dictionaries")

    boy_sign = _get_moon_sign(boy_chart)
    girl_sign = _get_moon_sign(girl_chart)

    breakdown = {}

    breakdown["Varna"] = _varna_score(boy_sign, girl_sign)
    breakdown["Vashya"] = _vashya_score(boy_sign, girl_sign)
    breakdown["Tara"] = _tara_score(boy_sign, girl_sign)
    breakdown["Yoni"] = _yoni_score(boy_sign, girl_sign)
    breakdown["Graha Maitri"] = _graha_maitri_score(boy_sign, girl_sign)
    breakdown["Gana"] = _gana_score(boy_sign, girl_sign)
    breakdown["Bhakoot"] = _bhakoot_score(boy_sign, girl_sign)
    breakdown["Nadi"] = _nadi_score(boy_sign, girl_sign)

    total_score = sum(breakdown.values())

    if total_score >= 30:
        compatibility = "Excellent"
    elif total_score >= 24:
        compatibility = "Good"
    elif total_score >= 18:
        compatibility = "Average"
    else:
        compatibility = "Challenging"

    mangal_status = _mangal_cross_check(boy_chart, girl_chart)

    return {
        "boy_moon_sign": boy_sign,
        "girl_moon_sign": girl_sign,
        "total_score": total_score,
        "max_score": 36,
        "compatibility_level": compatibility,
        "koota_breakdown": breakdown,
        "mangal_status": mangal_status
    }