# ==========================================================
# ⚠ DOSHA DETECTION ENGINE – FULLY STABILIZED VERSION
# ==========================================================

def detect_doshas(planets: dict, lagna: str = None):
    """
    Safe dosha detection engine.
    Accepts:
        planets (dict)
        lagna (optional)

    Returns structured dosha report.
    Never throws KeyError.
    """

    if not isinstance(planets, dict):
        raise TypeError("planets must be dictionary")

    doshas = []

    # ------------------------------------------------------
    # Safe extraction of planetary data
    # ------------------------------------------------------

    mars = planets.get("Mars", {})
    rahu = planets.get("Rahu", {})
    ketu = planets.get("Ketu", {})

    mars_house = mars.get("house")
    rahu_house = rahu.get("house")
    ketu_house = ketu.get("house")

    # ======================================================
    # 🔥 Mangal Dosha
    # Mars in 1,4,7,8,12
    # ======================================================

    if isinstance(mars_house, int) and mars_house in [1, 4, 7, 8, 12]:
        doshas.append("Mangal Dosha")

    # ======================================================
    # 🔥 Kaal Sarp Dosha (Simplified Logic)
    # Rahu & Ketu same house (symbolic simplified check)
    # ======================================================

    if (
        isinstance(rahu_house, int)
        and isinstance(ketu_house, int)
        and rahu_house == ketu_house
    ):
        doshas.append("Kaal Sarp Dosha (Simplified)")

    # ======================================================
    # 🔥 Optional Lagna Based Rule
    # ======================================================

    if lagna:
        if lagna == "Scorpio" and isinstance(mars_house, int) and mars_house == 1:
            doshas.append("Strong Mangal Influence (Lagna Based)")

    # ======================================================
    # SAFE DEFAULT
    # ======================================================

    if not doshas:
        doshas.append("No Major Dosha Detected")

    return {
        "lagna": lagna,
        "total_doshas": len(doshas),
        "doshas": doshas
    }