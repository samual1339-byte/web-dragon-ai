EXALTED_SIGNS = {
    "Sun": "Aries",
    "Moon": "Taurus",
    "Mars": "Capricorn",
    "Jupiter": "Cancer",
    "Venus": "Pisces",
    "Saturn": "Libra"
}


def calculate_strength(planets):
    for planet, data in planets.items():

        if planet in EXALTED_SIGNS and data["rashi"] == EXALTED_SIGNS[planet]:
            data["strength"] = "Exalted"
        elif data["house"] in [1, 5, 9]:
            data["strength"] = "Strong"
        else:
            data["strength"] = "Average"

    return planets
