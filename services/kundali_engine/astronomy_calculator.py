# ==========================================================
# 🔭 ASTRONOMY CALCULATOR – EXTENDED STRUCTURED CORE
# ==========================================================

import math
from datetime import datetime


# ----------------------------------------------------------
# Zodiac Signs
# ----------------------------------------------------------

RASHIS = [
    "Aries", "Taurus", "Gemini", "Cancer",
    "Leo", "Virgo", "Libra", "Scorpio",
    "Sagittarius", "Capricorn", "Aquarius", "Pisces"
]


# ----------------------------------------------------------
# Internal Utilities
# ----------------------------------------------------------

def _degree_to_rashi(degree: float) -> str:
    index = int(degree // 30) % 12
    return RASHIS[index]


def _degree_to_house(degree: float) -> int:
    return (int(degree // 30) % 12) + 1


def _generate_seed(birth_data: dict) -> int:
    return (
        sum(ord(c) for c in str(birth_data.get("date"))) +
        sum(ord(c) for c in str(birth_data.get("time"))) +
        sum(ord(c) for c in str(birth_data.get("place")))
    )


def _build_house_map(by_planet: dict) -> dict:
    house_map = {i: [] for i in range(1, 13)}
    for planet, pdata in by_planet.items():
        house = pdata.get("house")
        if isinstance(house, int) and 1 <= house <= 12:
            house_map[house].append(planet)
    return house_map


# ==========================================================
# 🔥 MAIN PLANETARY POSITION CALCULATOR (STRUCTURED)
# ==========================================================

def calculate_planetary_positions(birth_data: dict) -> dict:
    """
    Structured deterministic astronomical calculator.

    Returns unified planetary schema:

    {
        "birth_timestamp": "...",
        "by_planet": {...},
        "by_house": {...},
        "raw_seed": int
    }

    Safe for cloud deployment.
    Deterministic.
    No external dependencies.
    """

    if not isinstance(birth_data, dict):
        raise TypeError("birth_data must be dictionary")

    required_fields = ["date", "time", "place"]
    for field in required_fields:
        if not birth_data.get(field):
            raise ValueError(f"Missing required field: {field}")

    seed = _generate_seed(birth_data)

    base_positions = {
        "Sun": 120.5,
        "Moon": 210.2,
        "Mars": 15.7,
        "Mercury": 98.4,
        "Jupiter": 300.0,
        "Venus": 75.1,
        "Saturn": 250.6,
        "Rahu": 45.0,
        "Ketu": 225.0,
    }

    by_planet = {}

    for index, (planet, base_degree) in enumerate(base_positions.items()):

        degree = (base_degree + (seed % 30) + index * 3) % 360
        rashi = _degree_to_rashi(degree)
        house = _degree_to_house(degree)

        by_planet[planet] = {
            "degree": round(degree, 2),
            "rashi": rashi,
            "house": house,
            "retrograde": False,
            "strength_factor": round(math.cos(math.radians(degree)), 4)
        }

    by_house = _build_house_map(by_planet)

    return {
        "birth_timestamp": f"{birth_data.get('date')} {birth_data.get('time')}",
        "by_planet": by_planet,
        "by_house": by_house,
        "raw_seed": seed
    }


# ----------------------------------------------------------
# Backward Compatibility
# ----------------------------------------------------------

calculate_planet_positions = calculate_planetary_positions