from datetime import datetime

RASHIS = [
    "Aries", "Taurus", "Gemini", "Cancer",
    "Leo", "Virgo", "Libra", "Scorpio",
    "Sagittarius", "Capricorn", "Aquarius", "Pisces"
]


def _normalize_time(tob):
    """
    Ensures time is always HH:MM format.
    Prevents fluctuation due to seconds or malformed input.
    """

    if not tob:
        raise ValueError("Time of birth (tob) is required.")

    parts = tob.strip().split(":")

    if len(parts) < 2:
        raise ValueError("Invalid time format. Expected HH:MM")

    hour = int(parts[0])
    minute = int(parts[1])

    if hour < 0 or hour > 23:
        raise ValueError("Hour must be between 0 and 23.")

    if minute < 0 or minute > 59:
        raise ValueError("Minute must be between 0 and 59.")

    return hour, minute


def calculate_lagna(name, dob, tob, place):
    """
    Deterministic lagna calculation.
    Stable across servers.
    No system time.
    No timezone dependency.
    """

    hour, minute = _normalize_time(tob)

    # Stable Lagna Logic:
    # Using hour block only (12 zodiac division of 24h)
    lagna_index = hour % 12

    return RASHIS[lagna_index]