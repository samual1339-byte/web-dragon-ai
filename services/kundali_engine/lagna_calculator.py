# ==========================================================
# 🌅 LAGNA CALCULATOR – REAL SWISS EPHEMERIS ENGINE
# ==========================================================

import swisseph as swe
from datetime import datetime, timedelta
import math
import os


# ==========================================================
# 📍 RASHI LIST
# ==========================================================

RASHIS = [
    "Aries",
    "Taurus",
    "Gemini",
    "Cancer",
    "Leo",
    "Virgo",
    "Libra",
    "Scorpio",
    "Sagittarius",
    "Capricorn",
    "Aquarius",
    "Pisces"
]


# ==========================================================
# 📁 SET EPHEMERIS PATH
# ==========================================================

EPHE_PATH = os.path.join(
    os.path.dirname(__file__),
    "../ephemeris"
)

swe.set_ephe_path(EPHE_PATH)


# ==========================================================
# ⏱ TIME NORMALIZER
# ==========================================================

def normalize_time(tob):

    if not tob:
        raise ValueError("Time of birth required")

    parts = tob.strip().split(":")

    if len(parts) < 2:
        raise ValueError("Invalid time format HH:MM")

    hour = int(parts[0])
    minute = int(parts[1])

    if not (0 <= hour <= 23):
        raise ValueError("Hour invalid")

    if not (0 <= minute <= 59):
        raise ValueError("Minute invalid")

    return hour, minute


# ==========================================================
# 📅 DATE NORMALIZER
# ==========================================================

def normalize_date(dob):

    if not dob:
        raise ValueError("DOB required")

    dob = dob.replace("/", "-")

    parts = dob.split("-")

    if len(parts) != 3:
        raise ValueError("DOB must be YYYY-MM-DD")

    year = int(parts[0])
    month = int(parts[1])
    day = int(parts[2])

    return year, month, day


# ==========================================================
# 🌍 PLACE COORDINATE DATABASE (EXPANDABLE)
# ==========================================================

CITY_DATABASE = {

    "delhi": (28.6139, 77.2090),
    "mumbai": (19.0760, 72.8777),
    "kolkata": (22.5726, 88.3639),
    "chennai": (13.0827, 80.2707),
    "amritsar": (31.6340, 74.8723),
    "ludhiana": (30.9010, 75.8573),
    "chandigarh": (30.7333, 76.7794),
    "jaipur": (26.9124, 75.7873),
    "bangalore": (12.9716, 77.5946)

}


# ==========================================================
# 🌍 GET LATITUDE & LONGITUDE
# ==========================================================

def get_coordinates(place):

    if not place:
        raise ValueError("Place required")

    place = place.lower().strip()

    if place not in CITY_DATABASE:
        raise ValueError("Place not in database")

    return CITY_DATABASE[place]


# ==========================================================
# 🪐 JULIAN DAY CALCULATION
# ==========================================================

def get_julian_day(year, month, day, hour, minute):

    decimal_hour = hour + minute / 60.0

    jd = swe.julday(
        year,
        month,
        day,
        decimal_hour
    )

    return jd


# ==========================================================
# 🌅 ASCENDANT CALCULATION
# ==========================================================

def calculate_ascendant(jd, latitude, longitude):

    houses, ascmc = swe.houses_ex(
        jd,
        latitude,
        longitude,
        b'P'
    )

    asc_degree = ascmc[0]

    return asc_degree


# ==========================================================
# ♈ CONVERT DEGREE TO RASHI
# ==========================================================

def degree_to_rashi(degree):

    index = int(degree / 30)

    return RASHIS[index]


# ==========================================================
# 🌅 MAIN LAGNA ENGINE
# ==========================================================

def calculate_lagna(name, dob, tob, place):

    try:

        year, month, day = normalize_date(dob)

        hour, minute = normalize_time(tob)

        latitude, longitude = get_coordinates(place)

        jd = get_julian_day(
            year,
            month,
            day,
            hour,
            minute
        )

        asc_degree = calculate_ascendant(
            jd,
            latitude,
            longitude
        )

        lagna = degree_to_rashi(asc_degree)

        result = {

            "name": name,
            "ascendant": lagna,
            "ascendant_degree": round(asc_degree, 4),
            "latitude": latitude,
            "longitude": longitude,
            "julian_day": jd

        }

        return result

    except Exception as e:

        return {

            "error": str(e),
            "ascendant": "Aries"

        }