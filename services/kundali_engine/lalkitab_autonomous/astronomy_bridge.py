from ..astronomy_calculator import calculate_planet_positions
from ..lagna_calculator import calculate_lagna


def get_astronomy_data(birth_data):

    planets = calculate_planet_positions(birth_data)

    lagna = calculate_lagna(
        birth_data,
        planets
    )

    return planets, lagna
