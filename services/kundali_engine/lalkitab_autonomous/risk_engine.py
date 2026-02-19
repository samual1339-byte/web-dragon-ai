def calculate_risk(karmic, dosha, debt_cycle=None, pitru=None):

    score = 0

    # Base karmic risk
    if isinstance(karmic, dict):
        score += len(karmic) * 2

    # Dosha risk
    if isinstance(dosha, dict):
        score += len(dosha) * 3

    # Debt cycle severity
    if debt_cycle:
        for rin, value in debt_cycle.get("rin_severity_score", {}).items():
            score += value * 2

    # Pitru Dosha severity
    if pitru:
        if pitru.get("severity") == "High":
            score += 10
        elif pitru.get("severity") == "Moderate":
            score += 5

    # Normalize
    if score >= 25:
        return "Very High"
    elif score >= 15:
        return "High"
    elif score >= 8:
        return "Moderate"
    else:
        return "Low"