# ==========================================================
# 🔮 INTERPRETATION ENGINE – CLEAN STABLE VERSION
# ==========================================================

from datetime import datetime


def generate_interpretation(**kwargs):

    name = kwargs.get("name", "User")
    lagna = kwargs.get("lagna")
    strengths = kwargs.get("strengths", {})
    yogas = kwargs.get("yogas", [])
    doshas = kwargs.get("doshas", [])
    transit = kwargs.get("transit", {})

    summary_parts = []
    summary_parts.append(f"{name},")

    # ======================================================
    # Lagna Personality
    # ======================================================

    if not lagna:
        summary_parts.append("ascendant information is unavailable.")
    else:
        summary_parts.append(f"with {lagna} ascendant,")

        fire_signs = ["Leo", "Aries"]
        water_signs = ["Cancer", "Pisces"]
        practical_signs = [
            "Virgo",
            "Capricorn",
            "Taurus",
            "Gemini",
            "Libra",
            "Aquarius",
            "Sagittarius",
            "Scorpio",
        ]

        if lagna in fire_signs:
            summary_parts.append("you are bold and leadership-driven.")
        elif lagna in water_signs:
            summary_parts.append("you are emotional and intuitive.")
        elif lagna in practical_signs:
            summary_parts.append("you are practical and analytical.")
        else:
            summary_parts.append("your personality traits are unique and dynamic.")

    # ======================================================
    # Yogas
    # ======================================================

    yoga_list = []

    if isinstance(yogas, dict):
        yoga_list = yogas.get("yogas", [])
    elif isinstance(yogas, list):
        yoga_list = yogas

    if yoga_list:
        summary_parts.append(
            f"You have powerful yogas like {', '.join(yoga_list)}."
        )

    # ======================================================
    # Doshas
    # ======================================================

    dosha_list = []

    if isinstance(doshas, dict):
        dosha_list = doshas.get("doshas", [])
    elif isinstance(doshas, list):
        dosha_list = doshas

    if dosha_list:
        summary_parts.append(
            f"However, caution is advised due to {', '.join(dosha_list)}."
        )

    # ======================================================
    # Planetary Strength Analysis
    # ======================================================

    planetary_analysis = []

    if isinstance(strengths, dict):
        for planet, data in strengths.items():

            if not isinstance(data, dict):
                continue

            strength = data.get("strength", "Unknown")
            rashi = data.get("rashi", "Unknown")
            house = data.get("house")

            text = f"{planet} in {rashi}"

            if house:
                text += f" placed in house {house}"

            text += f" shows {strength} influence."

            planetary_analysis.append(text)

    if not planetary_analysis:
        planetary_analysis.append(
            "Detailed planetary strength data unavailable."
        )

    # ======================================================
    # Transit Analysis
    # ======================================================

    transit_analysis = []

    if isinstance(transit, dict):
        for planet, data in transit.items():

            if not isinstance(data, dict):
                continue

            rashi = data.get("rashi")
            house = data.get("house")

            text = f"Transit of {planet}"

            if rashi:
                text += f" in {rashi}"

            if house:
                text += f" affecting house {house}"

            text += " influences your current life phase."

            transit_analysis.append(text)

    if not transit_analysis:
        transit_analysis.append("Transit data not available.")

    # ======================================================
    # Final Output
    # ======================================================

    summary_text = " ".join(summary_parts)

    return {
        "summary": summary_text,
        "lagna": lagna,
        "planetary_analysis": planetary_analysis,
        "yoga_analysis": yoga_list if yoga_list else ["No major yoga detected."],
        "dosha_analysis": dosha_list if dosha_list else ["No major dosha detected."],
        "transit_analysis": transit_analysis,
        "generated_at": datetime.utcnow().isoformat(),
    }