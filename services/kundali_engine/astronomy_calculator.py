import random

PLANETS = ["Sun", "Moon", "Mars", "Mercury", "Jupiter", "Venus", "Saturn", "Rahu", "Ketu"]

RASHIS = [
    "Aries", "Taurus", "Gemini", "Cancer",
    "Leo", "Virgo", "Libra", "Scorpio",
    "Sagittarius", "Capricorn", "Aquarius", "Pisces"
]


def calculate_planetary_positions(name, dob, tob, place):
    """
    Temporary astronomical engine.
    Later replace with Swiss Ephemeris.
    """

    planets_data = {}

    for planet in PLANETS:
        degree = random.randint(0, 29)
        rashi_index = random.randint(0, 11)
        house = random.randint(1, 12)

        planets_data[planet] = {
            "rashi": RASHIS[rashi_index],
            "degree": degree,
            "house": house
        }

    return planets_data
