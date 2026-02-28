# ==========================================================
# 🌅 LAGNA CALCULATOR – FULLY STABILIZED VERSION
# ==========================================================

RASHIS = [
    "Aries", "Taurus", "Gemini", "Cancer",
    "Leo", "Virgo", "Libra", "Scorpio",
    "Sagittarius", "Capricorn", "Aquarius", "Pisces"
]


# ==========================================================
# 🔧 INTERNAL TIME NORMALIZER
# ==========================================================

def _normalize_time(tob: str):
    """
    Ensures time is HH:MM format.
    """

    if not tob:
        raise ValueError("Time of birth is required.")

    parts = tob.strip().split(":")

    if len(parts) < 2:
        raise ValueError("Invalid time format. Expected HH:MM")

    hour = int(parts[0])
    minute = int(parts[1])

    if not (0 <= hour <= 23):
        raise ValueError("Hour must be between 0 and 23")

    if not (0 <= minute <= 59):
        raise ValueError("Minute must be between 0 and 59")

    return hour, minute


# ==========================================================
# 🔥 MAIN LAGNA FUNCTION (MATCHES ENGINE CALL)
# ==========================================================

def calculate_lagna(name, dob, tob, place):
    """
    Deterministic Lagna Calculation.
    Accepts:
        name
        dob
        tob
        place

    Returns zodiac sign string.
    """

    # Only time is used for deterministic simplified logic
    hour, minute = _normalize_time(tob)

    # 24 hours divided into 12 rashis
    lagna_index = hour % 12

    return RASHIS[lagna_index]