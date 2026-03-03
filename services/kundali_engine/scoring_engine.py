# ==========================================================
# 📊 ADVANCED SCORING ENGINE – DESTINY ANALYTICS CORE v2
# ==========================================================

def calculate_scores(planets, strengths, yogas, doshas):

    score = {
        "planetary_strength_score": 0,
        "yoga_power_index": 0,
        "dosha_severity_index": 0,
        "career_index": 0,
        "marriage_index": 0,
        "wealth_index": 0,
        "spiritual_index": 0,
        "destiny_score": 0
    }

    # ------------------------------------------------------
    # SAFE NORMALIZER
    # ------------------------------------------------------

    def clamp(value):
        return max(0, min(100, round(value)))

    # ------------------------------------------------------
    # 1️⃣ PLANETARY STRENGTH SCORE (Weighted Model)
    # ------------------------------------------------------

    strength_weights = {
        "Exalted": 12,
        "Strong": 9,
        "Average": 6,
        "Weak": 3,
        "Debilitated": 1
    }

    total_strength = 0
    planet_count = 0

    if isinstance(strengths, dict):
        for planet, data in strengths.items():

            if not isinstance(data, dict):
                continue

            level = data.get("strength", "Average")
            weight = strength_weights.get(level, 5)

            total_strength += weight
            planet_count += 1

    if planet_count > 0:
        normalized_strength = (total_strength / (planet_count * 12)) * 100
        score["planetary_strength_score"] = clamp(normalized_strength)

    # ------------------------------------------------------
    # 2️⃣ YOGA POWER INDEX (Priority-Based Scaling)
    # ------------------------------------------------------

    yoga_score = 0

    if isinstance(yogas, dict):
        yogas = yogas.get("yogas", [])

    if isinstance(yogas, list):
        for yoga in yogas:

            yoga = str(yoga)

            if "Raj" in yoga:
                yoga_score += 20
            elif "Dhan" in yoga:
                yoga_score += 18
            elif "Gaja" in yoga or "Hams" in yoga:
                yoga_score += 15
            elif "Malavya" in yoga or "Ruchaka" in yoga:
                yoga_score += 14
            elif "Vipareet" in yoga:
                yoga_score += 16
            else:
                yoga_score += 8

    score["yoga_power_index"] = clamp(yoga_score)

    # ------------------------------------------------------
    # 3️⃣ DOSHA SEVERITY INDEX (Impact-Based Model)
    # ------------------------------------------------------

    dosha_score = 0

    if isinstance(doshas, dict):
        doshas = doshas.get("doshas", [])

    if isinstance(doshas, list):
        for dosha in doshas:

            dosha = str(dosha)

            if "Kaal" in dosha:
                dosha_score += 25
            elif "Manglik" in dosha or "Mangal" in dosha:
                dosha_score += 18
            elif "Shani" in dosha:
                dosha_score += 15
            elif "Rahu" in dosha or "Ketu" in dosha:
                dosha_score += 14
            else:
                dosha_score += 10

    score["dosha_severity_index"] = clamp(dosha_score)

    # ------------------------------------------------------
    # 4️⃣ DERIVED LIFE INDICES (Balanced Model)
    # ------------------------------------------------------

    strength = score["planetary_strength_score"]
    yoga_power = score["yoga_power_index"]
    dosha_severity = score["dosha_severity_index"]

    # Career Index (Leadership + Stability Bias)
    score["career_index"] = clamp(
        (strength * 0.45) +
        (yoga_power * 0.35) -
        (dosha_severity * 0.20)
    )

    # Marriage Index (Harmony Sensitive Model)
    score["marriage_index"] = clamp(
        (strength * 0.35) +
        (yoga_power * 0.20) -
        (dosha_severity * 0.45)
    )

    # Wealth Index (Prosperity Amplifier)
    score["wealth_index"] = clamp(
        (yoga_power * 0.50) +
        (strength * 0.40) -
        (dosha_severity * 0.10)
    )

    # Spiritual Index (Transformation Logic)
    score["spiritual_index"] = clamp(
        ((100 - dosha_severity) * 0.50) +
        (strength * 0.30) +
        (yoga_power * 0.20)
    )

    # ------------------------------------------------------
    # 5️⃣ FINAL DESTINY SCORE (Weighted Composite)
    # ------------------------------------------------------

    score["destiny_score"] = clamp(
        (
            score["career_index"] * 0.30 +
            score["marriage_index"] * 0.20 +
            score["wealth_index"] * 0.30 +
            score["spiritual_index"] * 0.20
        )
    )

    return score