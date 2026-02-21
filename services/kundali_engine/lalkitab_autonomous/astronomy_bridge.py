from ..astronomy_calculator import calculate_planet_positions
from ..lagna_calculator import calculate_lagna


def get_astronomy_data(birth_data):
    """
    Stable deterministic astronomy bridge.
    Ensures:
    - No dynamic system time usage
    - No missing birth parameters
    - Predictable output for same input
    """

    # ---------------------------------------------------
    # 1️⃣ Validate Required Birth Data
    # ---------------------------------------------------
    required_fields = ["date", "time", "place"]

    for field in required_fields:
        if field not in birth_data or not birth_data.get(field):
            raise ValueError(
                f"Missing required birth_data field: {field}"
            )

    # ---------------------------------------------------
    # 2️⃣ Calculate Planet Positions (Deterministic)
    # ---------------------------------------------------
    planets = calculate_planet_positions(birth_data)

    if not isinstance(planets, dict):
        raise TypeError(
            "calculate_planet_positions must return dictionary"
        )

    # Sort dictionary for consistent order
    planets = dict(sorted(planets.items()))

    # ---------------------------------------------------
    # 3️⃣ Calculate Lagna Based on Same Birth Data
    # ---------------------------------------------------
    lagna = calculate_lagna(
        birth_data,
        planets
    )

    if not lagna:
        raise ValueError("Lagna calculation failed.")

    # ---------------------------------------------------
    # 4️⃣ Final Stable Return
    # ---------------------------------------------------
    return planets, lagna