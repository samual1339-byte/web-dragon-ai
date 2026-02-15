from math import floor

def calculate_julian_day(year, month, day, hour, minute):
    if month <= 2:
        year -= 1
        month += 12

    A = floor(year / 100)
    B = 2 - A + floor(A / 4)

    jd_day = floor(365.25 * (year + 4716))
    jd_month = floor(30.6001 * (month + 1))

    jd = jd_day + jd_month + day + B - 1524.5
    jd += (hour + minute / 60) / 24

    return jd
