# ==========================================================
# 🧘 ADVANCED YOGA DETECTION ENGINE – ENTERPRISE VERSION
# ==========================================================

def detect_yogas(planets: dict, lagna: str = None):
    """
    Advanced, safe, scalable yoga detection engine.

    Parameters:
        planets (dict): planetary data dictionary
        lagna (str): ascendant sign

    Returns:
        dict:
            {
                "lagna": str,
                "total_yogas": int,
                "yogas": list,
                "details": list
            }
    """

    if not isinstance(planets, dict):
        raise TypeError("planets must be dictionary")

    # ------------------------------------------------------
    # Safe getters
    # ------------------------------------------------------

    def get_house(planet_name):
        pdata = planets.get(planet_name, {})
        return pdata.get("house") if isinstance(pdata, dict) else None

    def same_house(p1, p2):
        h1 = get_house(p1)
        h2 = get_house(p2)
        return isinstance(h1, int) and isinstance(h2, int) and h1 == h2

    def in_houses(planet, house_list):
        h = get_house(planet)
        return isinstance(h, int) and h in house_list

    yogas = []
    details = []

    kendra = [1, 4, 7, 10]
    trikona = [1, 5, 9]
    upachaya = [3, 6, 10, 11]
    dusthana = [6, 8, 12]

    # ======================================================
    # 🔥 SURYA-MANGAL YOGA
    # ======================================================

    if same_house("Sun", "Mars"):
        yogas.append("Surya-Mangal Yoga")
        details.append("Leadership power, authority and aggressive drive combined.")

    # ======================================================
    # 🌕 GAJA KESARI YOGA
    # ======================================================

    if in_houses("Moon", kendra) and in_houses("Jupiter", kendra):
        yogas.append("Gaja Kesari Yoga")
        details.append("Wisdom, fame, respect and protective fortune.")

    # ======================================================
    # 🧠 BUDH-ADITYA YOGA
    # ======================================================

    if same_house("Sun", "Mercury"):
        yogas.append("Budh-Aditya Yoga")
        details.append("Sharp intellect, business intelligence and communication strength.")

    # ======================================================
    # 💰 DHANA YOGA (Simplified)
    # 2nd and 11th house connection
    # ======================================================

    if in_houses("Jupiter", [2, 11]) or in_houses("Venus", [2, 11]):
        yogas.append("Dhana Yoga (Simplified)")
        details.append("Financial growth potential and resource accumulation.")

    # ======================================================
    # 🏛 RAJ YOGA (Simplified Kendra-Trikona Link)
    # ======================================================

    if (
        in_houses("Jupiter", trikona)
        and in_houses("Saturn", kendra)
    ):
        yogas.append("Raj Yoga (Simplified)")
        details.append("Authority, influence and high-status potential.")

    # ======================================================
    # 🔥 RUCHAKA YOGA (Mars in Kendra from Lagna)
    # ======================================================

    if lagna and in_houses("Mars", kendra):
        yogas.append("Ruchaka Yoga")
        details.append("Courage, dominance and warrior-like qualities.")

    # ======================================================
    # 🌊 HAMS YOGA (Jupiter in Kendra)
    # ======================================================

    if in_houses("Jupiter", kendra):
        yogas.append("Hams Yoga")
        details.append("Spiritual wisdom, righteousness and divine grace.")

    # ======================================================
    # 💎 MALAVYA YOGA (Venus in Kendra)
    # ======================================================

    if in_houses("Venus", kendra):
        yogas.append("Malavya Yoga")
        details.append("Luxury, beauty, comforts and artistic gifts.")

    # ======================================================
    # ⚔ SARALA YOGA (8th lord strength simplified)
    # ======================================================

    if in_houses("Mars", [8]) or in_houses("Saturn", [8]):
        yogas.append("Sarala Yoga (Simplified)")
        details.append("Resilience, overcoming obstacles and hidden strength.")

    # ======================================================
    # 🌑 VIPAREET RAJ YOGA (Dusthana planet in Dusthana)
    # ======================================================

    for planet in ["Saturn", "Mars", "Rahu", "Ketu"]:
        if in_houses(planet, dusthana):
            yogas.append("Vipareet Raj Yoga (Simplified)")
            details.append(f"{planet} in challenging house gives rise after struggle.")
            break

    # ======================================================
    # SAFE DEFAULT
    # ======================================================

    if not yogas:
        yogas.append("No Major Classical Yoga Detected")
        details.append("Chart appears balanced without dominant classical combinations.")

    # Remove duplicates safely
    yogas = list(dict.fromkeys(yogas))
    details = list(dict.fromkeys(details))

    return {
        "lagna": lagna,
        "total_yogas": len(yogas),
        "yogas": yogas,
        "details": details
    }