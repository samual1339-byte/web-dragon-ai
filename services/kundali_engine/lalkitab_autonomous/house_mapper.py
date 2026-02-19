from math import floor


def map_planets_to_houses(planets):

    house_map = {}

    for planet, degree in planets.items():
        house = floor(degree / 30) + 1
        house_map[planet] = house

    return house_map
