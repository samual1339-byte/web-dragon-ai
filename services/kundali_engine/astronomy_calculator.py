# ==========================================================
# 🔭 ASTRONOMY CALCULATOR – SWISS EPHEMERIS ENGINE
# Production Safe | Cloud Deployable | Structured Output
# ==========================================================

import swisseph as swe
import math
import os
from datetime import datetime


# ==========================================================
# EPHEMERIS PATH CONFIGURATION
# ==========================================================

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

EPHE_PATH = os.path.join(BASE_DIR, "ephemeris")

if os.path.exists(EPHE_PATH):
    swe.set_ephe_path(EPHE_PATH)


# ==========================================================
# ZODIAC SIGNS
# ==========================================================

RASHIS = [
    "Aries", "Taurus", "Gemini", "Cancer",
    "Leo", "Virgo", "Libra", "Scorpio",
    "Sagittarius", "Capricorn", "Aquarius", "Pisces"
]


# ==========================================================
# PLANET MAPPING (SWISS EPHEMERIS)
# ==========================================================

PLANETS = {
    "Sun": swe.SUN,
    "Moon": swe.MOON,
    "Mars": swe.MARS,
    "Mercury": swe.MERCURY,
    "Jupiter": swe.JUPITER,
    "Venus": swe.VENUS,
    "Saturn": swe.SATURN
}


# ==========================================================
# UTILITY FUNCTIONS
# ==========================================================

def _degree_to_rashi(degree: float) -> str:
    """Convert longitude degree to zodiac sign"""
    index = int(degree // 30) % 12
    return RASHIS[index]


def _degree_to_house(degree: float, ascendant: float) -> int:
    """Calculate house based on ascendant"""
    diff = (degree - ascendant) % 360
    house = int(diff // 30) + 1
    return house if house <= 12 else house % 12


def _build_house_map(by_planet: dict) -> dict:
    """Generate house → planets mapping"""

    house_map = {i: [] for i in range(1, 13)}

    for planet, pdata in by_planet.items():
        house = pdata.get("house")

        if isinstance(house, int) and 1 <= house <= 12:
            house_map[house].append(planet)

    return house_map


# ==========================================================
# JULIAN DAY CALCULATOR
# ==========================================================

def _calculate_julian_day(date_str: str, time_str: str) -> float:

    dt = datetime.strptime(f"{date_str} {time_str}", "%Y-%m-%d %H:%M")

    return swe.julday(
        dt.year,
        dt.month,
        dt.day,
        dt.hour + dt.minute / 60.0
    )


# ==========================================================
# ASCENDANT CALCULATOR
# ==========================================================

def _calculate_ascendant(jd, lat=28.6139, lon=77.2090):
    """
    Default coordinates: Delhi
    (You can upgrade later with geolocation API)
    """

    houses, ascmc = swe.houses(jd, lat, lon)

    ascendant_degree = ascmc[0]

    return ascendant_degree


# ==========================================================
# MAIN PLANETARY POSITION ENGINE
# ==========================================================

def calculate_planetary_positions(birth_data: dict) -> dict:

    if not isinstance(birth_data, dict):
        raise TypeError("birth_data must be dictionary")

    required_fields = ["date", "time", "place"]

    for field in required_fields:
        if not birth_data.get(field):
            raise ValueError(f"Missing required field: {field}")

    date = birth_data["date"]
    time = birth_data["time"]

    # ------------------------------------------------------
    # Julian Day
    # ------------------------------------------------------

    jd = _calculate_julian_day(date, time)

    # ------------------------------------------------------
    # Ascendant
    # ------------------------------------------------------

    ascendant_degree = _calculate_ascendant(jd)

    # ------------------------------------------------------
    # Planetary Calculations
    # ------------------------------------------------------

    by_planet = {}

    for planet_name, planet_code in PLANETS.items():

        result, flag = swe.calc_ut(jd, planet_code)

        longitude = result[0]
        speed = result[3]

        degree = longitude % 360

        rashi = _degree_to_rashi(degree)

        house = _degree_to_house(degree, ascendant_degree)

        retrograde = speed < 0

        by_planet[planet_name] = {
            "degree": round(degree, 4),
            "rashi": rashi,
            "house": house,
            "retrograde": retrograde,
            "speed": round(speed, 6),
            "strength_factor": round(math.cos(math.radians(degree)), 4)
        }

    # ------------------------------------------------------
    # Lunar Nodes (Rahu / Ketu)
    # ------------------------------------------------------

    rahu_data, flag = swe.calc_ut(jd, swe.MEAN_NODE)

    rahu_lon = rahu_data[0]

    ketu_lon = (rahu_lon + 180) % 360

    by_planet["Rahu"] = {
        "degree": round(rahu_lon, 4),
        "rashi": _degree_to_rashi(rahu_lon),
        "house": _degree_to_house(rahu_lon, ascendant_degree),
        "retrograde": True,
        "speed": 0,
        "strength_factor": round(math.cos(math.radians(rahu_lon)), 4)
    }

    by_planet["Ketu"] = {
        "degree": round(ketu_lon, 4),
        "rashi": _degree_to_rashi(ketu_lon),
        "house": _degree_to_house(ketu_lon, ascendant_degree),
        "retrograde": True,
        "speed": 0,
        "strength_factor": round(math.cos(math.radians(ketu_lon)), 4)
    }

    # ------------------------------------------------------
    # House Mapping
    # ------------------------------------------------------

    by_house = _build_house_map(by_planet)

    # ------------------------------------------------------
    # Final Structured Output
    # ------------------------------------------------------

    return {
        "birth_timestamp": f"{date} {time}",
        "ascendant_degree": round(ascendant_degree, 4),
        "ascendant_rashi": _degree_to_rashi(ascendant_degree),
        "by_planet": by_planet,
        "by_house": by_house
    }


# ==========================================================
# BACKWARD COMPATIBILITY
# ==========================================================

calculate_planet_positions = calculate_planetary_positions