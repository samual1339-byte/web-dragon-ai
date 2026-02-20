def calculate_risk(karmic, dosha, debt_cycle=None, pitru=None):

    score = 0
    breakdown = {
        "karmic_risk": 0,
        "dosha_risk": 0,
        "debt_cycle_risk": 0,
        "pitru_risk": 0
    }

    # --------------------------------------------------
    # 1️⃣ KARMIC RISK
    # --------------------------------------------------
    if isinstance(karmic, dict) and karmic:
        karmic_score = len(karmic) * 2
        score += karmic_score
        breakdown["karmic_risk"] = karmic_score

    # --------------------------------------------------
    # 2️⃣ DOSHA RISK
    # --------------------------------------------------
    if isinstance(dosha, dict) and dosha:
        dosha_score = len(dosha) * 3
        score += dosha_score
        breakdown["dosha_risk"] = dosha_score

    # --------------------------------------------------
    # 3️⃣ DEBT CYCLE SEVERITY
    # --------------------------------------------------
    if debt_cycle and isinstance(debt_cycle, dict):
        rin_scores = debt_cycle.get("rin_severity_score", {})
        for rin, value in rin_scores.items():
            debt_points = value * 2
            score += debt_points
            breakdown["debt_cycle_risk"] += debt_points

    # --------------------------------------------------
    # 4️⃣ PITRU DOSHA SEVERITY
    # --------------------------------------------------
    if pitru and isinstance(pitru, dict):
        severity = pitru.get("severity")
        if severity == "High":
            score += 10
            breakdown["pitru_risk"] = 10
        elif severity == "Moderate":
            score += 5
            breakdown["pitru_risk"] = 5

    # --------------------------------------------------
    # 5️⃣ NORMALIZATION
    # --------------------------------------------------
    if score >= 30:
        level = "Very High"
    elif score >= 20:
        level = "High"
    elif score >= 10:
        level = "Moderate"
    else:
        level = "Low"

    # --------------------------------------------------
    # 6️⃣ RETURN STRUCTURE (Backward Safe)
    # --------------------------------------------------

    return {
        "risk_level": level,          # OLD style equivalent
        "risk_score": score,          # NEW numeric score
        "risk_breakdown": breakdown   # Detailed intelligence
    }