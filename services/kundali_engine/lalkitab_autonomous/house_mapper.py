def map_planets_to_houses(planets):
    """
    Stable house mapper.

    Uses planetary degree (0–360 normalized)
    Maps each 30° block to 1–12 houses.
    Fully deterministic.
    Structure-safe.
    """

    if not isinstance(planets, dict):
        raise TypeError("Planets data must be dictionary.")

    house_map = {}

    for planet, data in planets.items():

        if not isinstance(data, dict):
            raise TypeError(f"Invalid planet data structure for {planet}")

        degree = float(data.get("degree", 0.0))
        degree = round(degree % 360, 4)

        house = int(degree // 30) + 1

        if house < 1:
            house = 1
        if house > 12:
            house = 12

        house_map[planet] = {
            "rashi": data.get("rashi"),
            "degree": degree,
            "house": house
        }

    return dict(sorted(house_map.items()))