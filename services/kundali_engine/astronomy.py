import datetime


class AstronomyEngine:

    @staticmethod
    def julian_day(date_obj):
        y = date_obj.year
        m = date_obj.month
        d = date_obj.day

        if m <= 2:
            y -= 1
            m += 12

        A = y // 100
        B = 2 - A + A // 4

        jd = int(365.25 * (y + 4716)) \
             + int(30.6001 * (m + 1)) \
             + d + B - 1524.5

        return jd

    @staticmethod
    def get_planet_positions(birth_data):

        date = birth_data["date"]
        time = birth_data["time"]

        dt = datetime.datetime.strptime(
            f"{date} {time}",
            "%Y-%m-%d %H:%M"
        )

        jd = AstronomyEngine.julian_day(dt)

        speeds = {
            "Sun": 0.9856,
            "Moon": 13.1764,
            "Mars": 0.524,
            "Mercury": 1.607,
            "Jupiter": 0.083,
            "Venus": 1.174,
            "Saturn": 0.033,
            "Rahu": -0.052,
            "Ketu": -0.052
        }

        planets = {}

        for planet, speed in speeds.items():
            degree = (jd * speed) % 360
            planets[planet] = {"degree": round(degree, 4)}

        return planets