# services/planets.py

def calculate_planet_position(julian_day, planet):
    """
    Simplified astronomical calculation (educational purpose)
    """

    base_positions = {
        "Sun": 280,
        "Moon": 218,
        "Mars": 150,
        "Mercury": 60,
        "Jupiter": 90,
        "Venus": 45,
        "Saturn": 300
    }

    daily_motion = {
        "Sun": 0.9856,
        "Moon": 13.1764,
        "Mars": 0.524,
        "Mercury": 1.607,
        "Jupiter": 0.083,
        "Venus": 1.174,
        "Saturn": 0.033
    }

    base = base_positions.get(planet, 0)
    motion = daily_motion.get(planet, 0)

    degree = (base + julian_day * motion) % 360
    return degree
