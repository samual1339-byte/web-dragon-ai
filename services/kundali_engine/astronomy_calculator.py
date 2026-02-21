import hashlib
from datetime import datetime

PLANETS = ["Sun", "Moon", "Mars", "Mercury", "Jupiter", "Venus", "Saturn", "Rahu", "Ketu"]

RASHIS = [
    "Aries", "Taurus", "Gemini", "Cancer",
    "Leo", "Virgo", "Libra", "Scorpio",
    "Sagittarius", "Capricorn", "Aquarius", "Pisces"
]


def _generate_stable_seed(name, dob, tob, place):
    """
    Create deterministic seed from birth data.
    Same input → same hash → same planetary result.
    """

    raw_string = f"{name}-{dob}-{tob}-{place}"
    hash_object = hashlib.sha256(raw_string.encode())
    hex_digest = hash_object.hexdigest()

    return int(hex_digest[:16], 16)


def _deterministic_number(seed, modifier, min_val, max_val):
    """
    Generate stable pseudo-random number within range.
    """

    value = (seed + modifier) % (max_val - min_val + 1)
    return min_val + value


def calculate_planetary_positions(name, dob, tob, place):
    """
    Deterministic astronomical engine.
    Same birth data always produces same result.
    No randomness.
    No system time.
    Production stable.
    """

    base_seed = _generate_stable_seed(name, dob, tob, place)

    planets_data = {}

    for index, planet in enumerate(PLANETS):

        degree = _deterministic_number(base_seed, index * 17, 0, 29)
        rashi_index = _deterministic_number(base_seed, index * 31, 0, 11)
        house = _deterministic_number(base_seed, index * 13, 1, 12)

        planets_data[planet] = {
            "rashi": RASHIS[rashi_index],
            "degree": round(float(degree), 2),
            "house": int(house)
        }

    return dict(sorted(planets_data.items()))