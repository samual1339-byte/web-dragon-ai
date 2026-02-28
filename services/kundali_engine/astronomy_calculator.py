# ==========================================================
# 🔭 ASTRONOMY CALCULATOR – STABLE CORE (DEPLOYMENT SAFE)
# ==========================================================

import math


# ----------------------------------------------------------
# Zodiac Signs
# ----------------------------------------------------------

RASHIS = [
    "Aries", "Taurus", "Gemini", "Cancer",
    "Leo", "Virgo", "Libra", "Scorpio",
    "Sagittarius", "Capricorn", "Aquarius", "Pisces"
]


# ----------------------------------------------------------
# Internal Degree → Rashi Converter
# ----------------------------------------------------------

def _degree_to_rashi(degree):
    index = int(degree // 30) % 12
    return RASHIS[index]


# ----------------------------------------------------------
# Internal Degree → House Calculator (Simplified)
# ----------------------------------------------------------

def _degree_to_house(degree):
    return (int(degree // 30) % 12) + 1


# ==========================================================
# 🔥 MAIN PLANETARY POSITION CALCULATOR
# ==========================================================

def calculate_planetary_positions(birth_data):
    """
    Deterministic mock astronomical calculator.

    - No external dependencies
    - No timezone dependency
    - Stable for cloud deployment
    - Returns structured planet dictionary
    """

    if not isinstance(birth_data, dict):
        raise TypeError("birth_data must be dictionary")

    required_fields = ["date", "time", "place"]

    for field in required_fields:
        if field not in birth_data or not birth_data.get(field):
            raise ValueError(f"Missing required field: {field}")

    # Stable base seed using birth date + time
    seed = sum(ord(c) for c in str(birth_data.get("date"))) + \
           sum(ord(c) for c in str(birth_data.get("time")))

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

    planets = {}

    for index, (planet, base_degree) in enumerate(base_positions.items()):

        # Add small deterministic variation
        degree = (base_degree + (seed % 30) + index * 3) % 360

        rashi = _degree_to_rashi(degree)
        house = _degree_to_house(degree)

        planets[planet] = {
            "degree": round(degree, 2),
            "rashi": rashi,
            "house": house
        }

    return planets


# ==========================================================
# 🔥 BACKWARD COMPATIBILITY FOR RENDER DEPLOYMENT
# ==========================================================

# If any module imports old name, it will still work
calculate_planet_positions = calculate_planetary_positions