def evaluate_pitru_dosha_lalkitab(house_map):
    """
    Deterministic Lal Kitab Pitru Dosha Evaluation.
    Compatible with structured house_map.
    Stable across environments.
    """

    if not isinstance(house_map, dict):
        raise TypeError("house_map must be dictionary")

    triggers = []
    ninth_house_planets = []

    # Safe extraction of house numbers
    for planet, data in house_map.items():
        if isinstance(data, dict):
            house = int(data.get("house", 0))
        else:
            house = int(data)

        if house == 9:
            ninth_house_planets.append(planet)

    # Specific triggers
    if "Sun" in ninth_house_planets:
        triggers.append("Sun in 9th House")

    if "Rahu" in ninth_house_planets:
        triggers.append("Rahu in 9th House")

    if "Saturn" in ninth_house_planets:
        triggers.append("Saturn in 9th House")

    # Malefic cluster logic
    malefics = {"Saturn", "Rahu", "Mars"}
    malefic_count = len(malefics.intersection(set(ninth_house_planets)))

    if malefic_count >= 2:
        triggers.append("Multiple Malefics in 9th House")

    # Severity calculation
    if malefic_count >= 2:
        severity = "High"
    elif len(triggers) == 1:
        severity = "Moderate"
    elif len(triggers) > 1:
        severity = "Elevated"
    else:
        severity = "None"

    return {
        "is_pitru_dosha": len(triggers) > 0,
        "severity": severity,
        "malefic_count": malefic_count,
        "ninth_house_planets": sorted(ninth_house_planets),
        "triggers": sorted(triggers)
    }