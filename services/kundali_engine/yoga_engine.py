# ==========================================================
# 🧘 YOGA DETECTION ENGINE – FULLY STABILIZED VERSION
# ==========================================================

def detect_yogas(planets: dict, lagna: str = None):
    """
    Safe yoga detection engine.
    Accepts:
        planets (dict)
        lagna (str, optional)

    Returns structured yoga report.
    Never throws KeyError.
    """

    if not isinstance(planets, dict):
        raise TypeError("planets must be dictionary")

    yogas = []

    # ------------------------------------------------------
    # Safe planetary extraction
    # ------------------------------------------------------

    sun = planets.get("Sun", {})
    mars = planets.get("Mars", {})
    jupiter = planets.get("Jupiter", {})
    moon = planets.get("Moon", {})

    sun_house = sun.get("house")
    mars_house = mars.get("house")
    jupiter_house = jupiter.get("house")
    moon_house = moon.get("house")

    # ======================================================
    # 🔥 Surya-Mangal Yoga
    # Sun and Mars in same house
    # ======================================================

    if isinstance(sun_house, int) and isinstance(mars_house, int):
        if sun_house == mars_house:
            yogas.append("Surya-Mangal Yoga")

    # ======================================================
    # 🔥 Gaja Kesari Yoga
    # Moon and Jupiter in Kendra (1,4,7,10)
    # ======================================================

    kendra_houses = [1, 4, 7, 10]

    if (
        isinstance(jupiter_house, int)
        and isinstance(moon_house, int)
        and jupiter_house in kendra_houses
        and moon_house in kendra_houses
    ):
        yogas.append("Gaja Kesari Yoga")

    # ======================================================
    # 🔥 Simple Lagna-Based Yoga (Optional Support)
    # ======================================================

    if lagna:
        if lagna == "Aries" and isinstance(mars_house, int) and mars_house == 1:
            yogas.append("Ruchaka Yoga (Simplified)")

    # ======================================================
    # SAFE DEFAULT
    # ======================================================

    if not yogas:
        yogas.append("No Major Yoga Detected")

    return {
        "lagna": lagna,
        "total_yogas": len(yogas),
        "yogas": yogas
    }