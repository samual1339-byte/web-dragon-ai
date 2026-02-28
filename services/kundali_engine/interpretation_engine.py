# ==========================================================
# 🔮 INTERPRETATION ENGINE – EXPANDED & STABILIZED VERSION
# ==========================================================

from datetime import datetime


def generate_interpretation(**kwargs):
    """
    Expanded interpretation engine compatible with
    Kundali master engine structure.

    Accepts flexible keyword arguments:
        name
        lagna
        planets
        strengths
        yogas
        doshas
        transit
    """

    name = kwargs.get("name", "User")
    lagna = kwargs.get("lagna")
    planets = kwargs.get("planets", {})
    strengths = kwargs.get("strengths", {})
    yogas = kwargs.get("yogas", {})
    doshas = kwargs.get("doshas", {})
    transit = kwargs.get("transit", {})

    summary_text = f"{name}, "

    # ------------------------------------------------------
    # Lagna Personality Logic (Your Original Logic Expanded)
    # ------------------------------------------------------

    if lagna:
        summary_text += f"with {lagna} ascendant, "

        if lagna in ["Leo", "Aries"]:
            summary_text += "you are bold and leadership-driven. "
        elif lagna in ["Cancer", "Pisces"]:
            summary_text += "you are emotional and intuitive. "
        else:
            summary_text += "you are practical and analytical. "
    else:
        summary_text += "ascendant information is unavailable. "

    # ------------------------------------------------------
    # Yoga Handling (Structured Compatible)
    # ------------------------------------------------------

    yoga_list = []

    if isinstance(yogas, dict):
        yoga_list = yogas.get("yogas", [])
    elif isinstance(yogas, list):
        yoga_list = yogas

    if yoga_list:
        summary_text += f"You have powerful yogas like {', '.join(yoga_list)}. "

    # ------------------------------------------------------
    # Dosha Handling
    # ------------------------------------------------------

    dosha_list = []

    if isinstance(doshas, dict):
        dosha_list = doshas.get("doshas", [])
    elif isinstance(doshas, list):
        dosha_list = doshas

    if dosha_list:
        summary_text += f"However, caution due to {', '.join(dosha_list)}. "

    # ------------------------------------------------------
    # Planetary Strength Expansion
    # ------------------------------------------------------

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
        planetary_analysis.append("Detailed planetary strength data unavailable.")

    # ------------------------------------------------------
    # Transit Expansion
    # ------------------------------------------------------

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

    # ------------------------------------------------------
    # Final Structured Output
    # ------------------------------------------------------

    return {
        "summary": summary_text,
        "lagna": lagna,
        "planetary_analysis": planetary_analysis,
        "yoga_analysis": yoga_list if yoga_list else ["No major yoga detected."],
        "dosha_analysis": dosha_list if dosha_list else ["No major dosha detected."],
        "transit_analysis": transit_analysis,
        "generated_at": datetime.utcnow().isoformat()
    }