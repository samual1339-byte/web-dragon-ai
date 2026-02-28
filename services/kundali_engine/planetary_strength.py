# ==========================================================
# 🌟 PLANETARY STRENGTH ENGINE – FULLY STABILIZED VERSION
# ==========================================================

RASHIS = [
    "Aries", "Taurus", "Gemini", "Cancer",
    "Leo", "Virgo", "Libra", "Scorpio",
    "Sagittarius", "Capricorn", "Aquarius", "Pisces"
]


EXALTED_SIGNS = {
    "Sun": "Aries",
    "Moon": "Taurus",
    "Mars": "Capricorn",
    "Jupiter": "Cancer",
    "Venus": "Pisces",
    "Saturn": "Libra"
}


# ==========================================================
# 🔧 INTERNAL RASHI DERIVATION (FROM DEGREE)
# ==========================================================

def _derive_rashi_from_degree(degree):
    """
    Converts 0–360 degree value into zodiac sign.
    Each sign occupies 30 degrees.
    """

    if degree is None:
        return None

    try:
        degree = float(degree)
    except (TypeError, ValueError):
        return None

    index = int(degree // 30) % 12
    return RASHIS[index]


# ==========================================================
# 🌟 MAIN STRENGTH CALCULATOR
# ==========================================================

def calculate_strength(planets: dict):
    """
    Safe planetary strength evaluation.
    Never throws KeyError.
    Returns new structured dictionary.
    """

    if not isinstance(planets, dict):
        raise TypeError("planets must be dictionary")

    strength_result = {}

    for planet, data in planets.items():

        if not isinstance(data, dict):
            continue

        degree = data.get("degree")
        rashi = data.get("rashi")
        house = data.get("house")

        # 🔥 Auto derive rashi if missing
        if not rashi and degree is not None:
            rashi = _derive_rashi_from_degree(degree)

        # Default strength
        strength = "Average"

        # 🔥 Exalted check
        if planet in EXALTED_SIGNS and rashi == EXALTED_SIGNS[planet]:
            strength = "Exalted"

        # 🔥 House strength check (only if house exists)
        elif isinstance(house, int) and house in [1, 5, 9]:
            strength = "Strong"

        # 🔥 If completely missing data
        if not rashi and house is None:
            strength = "Unknown"

        # 🔥 Construct safe output
        strength_result[planet] = {
            "degree": degree,
            "rashi": rashi,
            "house": house,
            "strength": strength
        }

    return strength_result