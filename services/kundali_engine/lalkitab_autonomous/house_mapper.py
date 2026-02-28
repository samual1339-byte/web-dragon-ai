def map_planets_to_houses(planets):
    """
    Stable & tolerant house mapper.

    Accepts:
        - dict of planets
        - list of planet dictionaries
    Always returns safe structured dictionary.
    Never crashes.
    """

    if not planets:
        return {}

    # --------------------------------------------------
    # 1️⃣ Normalize Structure
    # --------------------------------------------------

    normalized = {}

    # Case A: Already dictionary
    if isinstance(planets, dict):
        for planet, data in planets.items():
            if isinstance(data, dict):
                normalized[planet] = data

    # Case B: List of dicts → convert to dict
    elif isinstance(planets, list):
        for item in planets:
            if isinstance(item, dict) and "planet" in item:
                normalized[item["planet"]] = item

    else:
        # Unsupported structure → fail safe
        return {}

    # --------------------------------------------------
    # 2️⃣ Safe House Mapping
    # --------------------------------------------------

    house_map = {}

    for planet, data in normalized.items():

        try:
            degree = float(data.get("degree", 0.0))
        except (ValueError, TypeError):
            degree = 0.0

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