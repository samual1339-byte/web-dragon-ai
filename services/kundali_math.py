from services.julian_day import calculate_julian_day
from services.planets import calculate_planet_position
from services.rashi import get_rashi


def generate_real_kundali(dob, tob):
    year, month, day = map(int, dob.split("-"))
    hour, minute = map(int, tob.split(":"))

    jd = calculate_julian_day(year, month, day, hour, minute)

    kundali = {}

    for planet in ["Sun", "Moon", "Mars", "Mercury", "Jupiter", "Venus", "Saturn"]:
        degree = calculate_planet_position(jd, planet)
        kundali[planet] = {
            "degree": round(degree, 2),
            "rashi": get_rashi(degree)
        }

    return kundali
