"""
interpretation_engine.py

Unified Advanced Narrative Engine
Structured for:

- Birth Chart Interpretation
- Current Transit Interpretation
- House-wise Analysis
- Lal Kitab Impact Layer
- AI Insight Layer
- Remedies Layer
- Structured API Output
"""

from datetime import datetime


# ==========================================================
# UTILITIES
# ==========================================================

def _clamp(value, minimum=0, maximum=100):
    return max(minimum, min(maximum, value))


def _safe_list(value):
    if isinstance(value, dict):
        return value.get("yogas") or value.get("doshas") or []
    return value if isinstance(value, list) else []


# ==========================================================
# PERSONALITY SUMMARY
# ==========================================================

def _generate_lagna_summary(name: str, lagna: str):

    if not lagna or lagna == "Unknown":
        return "Ascendant information unavailable."

    prefix = f"{name}, " if name else ""

    elements = {
        "Fire": ["Aries", "Leo", "Sagittarius"],
        "Earth": ["Taurus", "Virgo", "Capricorn"],
        "Air": ["Gemini", "Libra", "Aquarius"],
        "Water": ["Cancer", "Scorpio", "Pisces"]
    }

    if lagna in elements["Fire"]:
        trait = "dynamic, leadership-driven and action oriented"
    elif lagna in elements["Earth"]:
        trait = "stable, practical and materially grounded"
    elif lagna in elements["Air"]:
        trait = "intellectual, communicative and strategic"
    elif lagna in elements["Water"]:
        trait = "intuitive, emotionally perceptive and spiritually sensitive"
    else:
        trait = "balanced and adaptive in nature"

    return f"{prefix}with {lagna} ascendant, you are naturally {trait}."


# ==========================================================
# PLANETARY POSITION INTERPRETATION
# ==========================================================

def _interpret_planetary_positions(by_planet: dict):

    interpretations = []

    for planet, pdata in by_planet.items():

        house = pdata.get("house")
        rashi = pdata.get("rashi")
        degree = pdata.get("degree")

        line = (
            f"{planet} positioned in {rashi} (House {house}) "
            f"at {degree}° influences life themes related to house {house} matters."
        )

        interpretations.append(line)

    return interpretations


# ==========================================================
# YOGA ANALYSIS
# ==========================================================

def _interpret_yogas(yogas):

    yogas = _safe_list(yogas)

    if not yogas:
        return {
            "count": 0,
            "details": [],
            "summary": "No dominant classical yogas detected."
        }

    return {
        "count": len(yogas),
        "details": yogas,
        "summary": f"{len(yogas)} auspicious yogas enhance destiny."
    }


# ==========================================================
# DOSHA ANALYSIS
# ==========================================================

def _interpret_doshas(doshas):

    doshas = _safe_list(doshas)

    if not doshas or "No Major Dosha Detected" in doshas:
        return {
            "count": 0,
            "details": [],
            "summary": "No significant dosha affecting core life areas."
        }

    return {
        "count": len(doshas),
        "details": doshas,
        "summary": f"{len(doshas)} karmic imbalance factors require awareness."
    }


# ==========================================================
# LAL KITAB IMPACT LAYER (FIXED)
# ==========================================================

def _generate_lalkitab_layer(by_planet: dict):

    impacts = []
    remedies = []

    for planet, pdata in by_planet.items():

        house = pdata.get("house")

        if house in [6, 8, 12]:
            impacts.append(
                f"{planet} in house {house} indicates karmic debt activation."
            )
            remedies.append(
                f"Perform donation related to {planet} on its weekday."
            )

    if not impacts:
        impacts.append("No strong Lal Kitab karmic triggers detected.")

    if not remedies:
        remedies.append("Maintain ethical conduct and balanced routine.")

    return {
        "impact_analysis": impacts,
        "remedies": remedies
    }


# ==========================================================
# AI GENERATED INSIGHT LAYER
# ==========================================================

def _generate_ai_insight(yoga_count, dosha_count, strengths):

    score = 60
    score += yoga_count * 5
    score -= dosha_count * 6

    if isinstance(strengths, dict):
        for pdata in strengths.values():
            if isinstance(pdata, dict):
                if pdata.get("strength") in ["Strong", "Exalted"]:
                    score += 2
                if pdata.get("strength") in ["Weak", "Debilitated"]:
                    score -= 2

    destiny_score = _clamp(score)

    if destiny_score >= 75:
        impact = "High growth potential with strong karmic momentum."
    elif destiny_score >= 55:
        impact = "Balanced life with moderate rise and learning phases."
    else:
        impact = "Life requires structured effort and conscious correction."

    return {
        "destiny_score": destiny_score,
        "ai_kundali_impact": impact
    }


# ==========================================================
# TRANSIT INTERPRETATION
# ==========================================================

def _interpret_transits(current_planets: dict):

    if not current_planets:
        return "Current transit data unavailable."

    active = []

    for planet, pdata in current_planets.items():
        house = pdata.get("house")
        active.append(f"{planet} currently influencing house {house} themes.")

    return " ".join(active)


# ==========================================================
# MAIN ENGINE
# ==========================================================

def generate_interpretation(
    birth_planetary_data: dict,
    current_planetary_data: dict,
    strengths: dict,
    yogas,
    doshas,
    lagna: str,
    name: str = None
):

    try:

        birth_by_planet = birth_planetary_data.get("by_planet", {})
        current_by_planet = current_planetary_data.get("by_planet", {})

        personality = _generate_lagna_summary(name, lagna)

        planetary_birth = _interpret_planetary_positions(birth_by_planet)

        yoga_data = _interpret_yogas(yogas)
        dosha_data = _interpret_doshas(doshas)

        lalkitab_layer = _generate_lalkitab_layer(birth_by_planet)

        ai_layer = _generate_ai_insight(
            yoga_data["count"],
            dosha_data["count"],
            strengths
        )

        transit_layer = _interpret_transits(current_by_planet)

        return {
            "birth_chart": {
                "personality_summary": personality,
                "planetary_positions": planetary_birth,
                "yoga_analysis": yoga_data,
                "dosha_analysis": dosha_data,
                "lalkitab": lalkitab_layer
            },
            "current_transit": {
                "transit_influence": transit_layer
            },
            "ai_analysis": ai_layer,
            "generated_at": datetime.utcnow().isoformat()
        }

    except Exception as e:
        return {
            "error": str(e),
            "generated_at": datetime.utcnow().isoformat()
        }