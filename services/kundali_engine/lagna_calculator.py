from datetime import datetime

RASHIS = [
    "Aries", "Taurus", "Gemini", "Cancer",
    "Leo", "Virgo", "Libra", "Scorpio",
    "Sagittarius", "Capricorn", "Aquarius", "Pisces"
]


def calculate_lagna(name, dob, tob, place):
    """
    Simple time-based lagna logic.
    Replace with astronomical ascendant math later.
    """

    hour = int(tob.split(":")[0])
    lagna_index = hour % 12
    return RASHIS[lagna_index]
