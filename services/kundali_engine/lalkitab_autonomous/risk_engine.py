def calculate_risk(karmic, dosha, debt_cycle=None, pitru=None):
    """
    Deterministic Risk Calculation Engine.
    Structure-aware.
    Severity-aware.
    Stable across environments.
    """

    total_score = 0

    breakdown = {
        "karmic_risk": 0,
        "dosha_risk": 0,
        "debt_cycle_risk": 0,
        "pitru_risk": 0
    }

    # --------------------------------------------------
    # 1️⃣ KARMIC RISK (Only count active flags)
    # --------------------------------------------------
    if isinstance(karmic, dict) and karmic:

        active_karmic = [
            key for key, value in karmic.items()
            if value not in (None, False, {}, [])
        ]

        karmic_score = len(active_karmic) * 2
        breakdown["karmic_risk"] = karmic_score
        total_score += karmic_score

    # --------------------------------------------------
    # 2️⃣ DOSHA RISK (Structured evaluation)
    # --------------------------------------------------
    if isinstance(dosha, dict) and dosha:

        dosha_score = 0

        # Pitru dosha handled separately below
        for key, value in dosha.items():

            if isinstance(value, dict):
                if value.get("active") is True:
                    dosha_score += 4
            elif key.startswith("is_") and value is True:
                dosha_score += 4

        breakdown["dosha_risk"] = dosha_score
        total_score += dosha_score

    # --------------------------------------------------
    # 3️⃣ DEBT CYCLE RISK
    # --------------------------------------------------
    if isinstance(debt_cycle, dict):

        rin_scores = debt_cycle.get("rin_severity_score", {})

        if isinstance(rin_scores, dict):
            for rin in sorted(rin_scores.keys()):
                value = rin_scores.get(rin)

                if isinstance(value, (int, float)) and value > 0:
                    debt_points = int(value) * 2
                    breakdown["debt_cycle_risk"] += debt_points
                    total_score += debt_points

    # --------------------------------------------------
    # 4️⃣ PITRU DOSHA SEVERITY (Structured)
    # --------------------------------------------------
    if isinstance(pitru, dict):

        severity = pitru.get("severity", "None")

        if severity == "High":
            breakdown["pitru_risk"] = 10
            total_score += 10
        elif severity == "Elevated":
            breakdown["pitru_risk"] = 7
            total_score += 7
        elif severity == "Moderate":
            breakdown["pitru_risk"] = 5
            total_score += 5

    # --------------------------------------------------
    # 5️⃣ NORMALIZATION SCALE
    # --------------------------------------------------
    if total_score >= 40:
        level = "Critical"
    elif total_score >= 30:
        level = "Very High"
    elif total_score >= 20:
        level = "High"
    elif total_score >= 10:
        level = "Moderate"
    else:
        level = "Low"

    # --------------------------------------------------
    # 6️⃣ FINAL STRUCTURED OUTPUT
    # --------------------------------------------------

    return {
        "risk_level": level,
        "risk_score": int(total_score),
        "risk_breakdown": breakdown
    }