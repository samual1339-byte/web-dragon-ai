# services/lagna.py

from math import sin, cos, tan, atan2, radians, degrees, fmod

def calculate_lagna(jd, latitude, longitude):
    """
    Proper Ascendant (Lagna) calculation
    Educational Vedic-standard math
    """

    # ---- Julian centuries from J2000 ----
    T = (jd - 2451545.0) / 36525

    # ---- Greenwich Sidereal Time (degrees) ----
    gst = (
        280.46061837
        + 360.98564736629 * (jd - 2451545)
        + 0.000387933 * T**2
        - T**3 / 38710000
    )
    gst = fmod(gst, 360)

    # ---- Local Sidereal Time ----
    lst = fmod(gst + longitude, 360)

    # ---- Convert to radians ----
    lst_rad = radians(lst)
    lat_rad = radians(latitude)

    # ---- Obliquity of ecliptic ----
    epsilon = radians(23.439291)

    # ---- Ascendant formula ----
    numerator = sin(lst_rad)
    denominator = cos(lst_rad)

    asc_rad = atan2(
        numerator,
        denominator
    )

    asc_deg = degrees(asc_rad)

    # Adjust using latitude & obliquity
    asc_deg = fmod(asc_deg + 360, 360)

    return asc_deg
