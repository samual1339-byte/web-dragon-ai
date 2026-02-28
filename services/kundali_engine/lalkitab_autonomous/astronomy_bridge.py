# ==========================================================
# 🌌 ASTRONOMY BRIDGE – FULLY STABILIZED VERSION
# ==========================================================

from ..astronomy_calculator import calculate_planetary_positions
from ..lagna_calculator import calculate_lagna


def get_astronomy_data(birth_data):
    """
    Stable deterministic astronomy bridge.

    Ensures:
    - Required birth fields are present
    - No system time dependency
    - Consistent deterministic output
    - Structured (planets, lagna) return
    """

    # =====================================================
    # 1️⃣ Validate Required Birth Data
    # =====================================================

    if not isinstance(birth_data, dict):
        raise TypeError("birth_data must be dictionary")

    required_fields = ["name", "date", "time", "place"]

    for field in required_fields:
        if field not in birth_data or not birth_data.get(field):
            raise ValueError(
                f"Missing required birth_data field: {field}"
            )

    # =====================================================
    # 2️⃣ Calculate Planet Positions
    # =====================================================

    planets = calculate_planetary_positions(birth_data)

    if not isinstance(planets, dict):
        raise TypeError(
            "calculate_planetary_positions must return dictionary"
        )

    # Sort planets for deterministic order
    planets = dict(sorted(planets.items()))

    # =====================================================
    # 3️⃣ Calculate Lagna Separately
    # =====================================================

    lagna = calculate_lagna(
        birth_data.get("name"),
        birth_data.get("date"),
        birth_data.get("time"),
        birth_data.get("place")
    )

    if not lagna:
        raise ValueError("Lagna calculation failed")

    # =====================================================
    # 4️⃣ Final Structured Return
    # =====================================================

    return planets, lagna