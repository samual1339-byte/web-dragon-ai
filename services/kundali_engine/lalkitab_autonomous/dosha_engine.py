def check_lalkitab_pitru_dosha(kundali):

    triggers = []

    if kundali.get("Sun") == 9:
        triggers.append("Sun in 9th House")

    if kundali.get("Rahu") == 9:
        triggers.append("Rahu in 9th House")

    if kundali.get("Saturn") == 9:
        triggers.append("Saturn in 9th House")

    malefics = ["Saturn", "Rahu", "Mars"]
    count = sum(1 for p in malefics if kundali.get(p) == 9)

    if count >= 2:
        triggers.append("Multiple malefics in 9th")

    return {
        "is_pitru_dosha": len(triggers) > 0,
        "severity": "High" if len(triggers) >= 2 else "Moderate" if len(triggers) == 1 else "None",
        "triggers": triggers
    }
def evaluate_pitru_dosha_lalkitab(house_map):

    triggers = []

    if house_map.get("Sun") == 9:
        triggers.append("Sun in 9th")

    if house_map.get("Rahu") == 9:
        triggers.append("Rahu in 9th")

    if house_map.get("Saturn") == 9:
        triggers.append("Saturn in 9th")

    malefics = ["Saturn", "Rahu", "Mars"]
    count = sum(1 for p in malefics if house_map.get(p) == 9)

    if count >= 2:
        triggers.append("Multiple malefics in 9th")

    return {
        "is_pitru_dosha": len(triggers) > 0,
        "severity": "High" if len(triggers) >= 2 else "Moderate" if len(triggers) == 1 else "None",
        "triggers": triggers
    }