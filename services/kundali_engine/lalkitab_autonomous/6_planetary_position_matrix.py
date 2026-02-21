PLANETS = ["Sun","Moon","Mars","Mercury","Jupiter","Venus","Saturn","Rahu","Ketu"]

HOUSES = list(range(1,13))


def _generate_matrix():

    matrix = {}

    for planet in PLANETS:

        matrix[planet] = {}

        for house in HOUSES:

            # -----------------------------
            # Base Nature Logic
            # -----------------------------

            if planet in ["Sun","Mars","Saturn"]:
                temperament = "Strong karmic influence"
                base_risk = 3
            elif planet in ["Rahu","Ketu"]:
                temperament = "Shadow karmic influence"
                base_risk = 4
            else:
                temperament = "Supportive karmic influence"
                base_risk = 2

            # -----------------------------
            # House Category Logic
            # -----------------------------

            if house in [1,4,7,10]:
                house_type = "Kendra"
                modifier = 1
            elif house in [5,9]:
                house_type = "Trikona"
                modifier = -1
            elif house in [6,8,12]:
                house_type = "Dusthana"
                modifier = 2
            else:
                house_type = "Neutral"
                modifier = 0

            risk_weight = max(1, base_risk + modifier)

            # -----------------------------
            # Construct Meaning
            # -----------------------------

            core_nature = f"{planet} in {house_type} house {house}"

            positive_effects = [
                f"{planet} strengthens themes of house {house}",
                "Life lessons bring maturity",
                "Potential for growth through discipline"
            ]

            negative_effects = []

            if house in [6,8,12]:
                negative_effects.append("Hidden obstacles and karmic trials")

            if planet in ["Rahu","Ketu"]:
                negative_effects.append("Illusion and confusion phases")

            if planet == "Saturn":
                negative_effects.append("Delays and heavy responsibilities")

            karmic_theme = f"{planet} karma activated in house {house}"

            # -----------------------------
            # Remedies
            # -----------------------------

            remedy_map = {
                "Sun": "Offer water to Sun at sunrise.",
                "Moon": "Donate rice or milk on Mondays.",
                "Mars": "Donate red lentils on Tuesdays.",
                "Mercury": "Donate green items on Wednesdays.",
                "Jupiter": "Donate yellow sweets on Thursdays.",
                "Venus": "Donate white sweets on Fridays.",
                "Saturn": "Donate black sesame on Saturdays.",
                "Rahu": "Donate coconut and avoid deception.",
                "Ketu": "Feed stray dogs and meditate."
            }

            matrix[planet][house] = {
                "core_nature": core_nature,
                "positive_effects": positive_effects,
                "negative_effects": negative_effects,
                "karmic_theme": karmic_theme,
                "risk_weight": risk_weight,
                "remedy": remedy_map.get(planet)
            }

    return matrix


PLANET_POSITION_MATRIX = _generate_matrix()