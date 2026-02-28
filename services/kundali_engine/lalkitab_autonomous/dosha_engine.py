def evaluate_dosha(house_map):

    if not isinstance(house_map, dict):
        raise TypeError("house_map must be dictionary")

    return {}  # minimal safe implementation


def evaluate_pitru_dosha_lalkitab(house_map):

    if not isinstance(house_map, dict):
        raise TypeError("house_map must be dictionary")

    return {
        "is_pitru_dosha": False,
        "severity": "None",
        "severity_score": 0,
        "ninth_house_planets": [],
        "second_house_planets": [],
        "first_house_planets": [],
        "malefic_count_in_9th": 0,
        "triggers": []
    }