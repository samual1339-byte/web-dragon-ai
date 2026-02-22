import copy


# ==========================================================
# 🔥 KARMIC STRUCTURE EVALUATION
# ==========================================================

def evaluate_karmic_structure(house_map):

    karmic_flags = {}

    for planet, data in house_map.items():

        house = data.get("house")

        if house in [6, 8, 12]:
            karmic_flags[planet] = {
                "house": house,
                "karmic_intensity": "High",
                "theme": "Past life unresolved karma"
            }

        elif house in [1, 5, 9]:
            karmic_flags[planet] = {
                "house": house,
                "karmic_intensity": "Positive",
                "theme": "Dharma activation"
            }

        else:
            karmic_flags[planet] = {
                "house": house,
                "karmic_intensity": "Neutral",
                "theme": "Material life experience"
            }

    return dict(sorted(karmic_flags.items()))


# ==========================================================
# 🔁 HOUSE EXCHANGE LOGIC
# ==========================================================

def detect_house_exchange(house_map):

    exchanges = []

    planets = list(house_map.keys())

    for i in range(len(planets)):
        for j in range(i + 1, len(planets)):

            p1 = planets[i]
            p2 = planets[j]

            h1 = house_map[p1].get("house")
            h2 = house_map[p2].get("house")

            if h1 == h2:
                continue

            if (
                house_map.get(p1, {}).get("house") ==
                house_map.get(p2, {}).get("house")
            ):
                exchanges.append({
                    "planet_1": p1,
                    "planet_2": p2,
                    "type": "Direct Exchange"
                })

    return exchanges


# ==========================================================
# 💰 DEBT CYCLE (RIN LOGIC)
# ==========================================================

def evaluate_debt_cycle(house_map, planetary_db):

    rin_report = {}
    score_map = {"Low": 1, "Medium": 2, "High": 3}

    for planet, data in house_map.items():

        house = data.get("house")

        rule = planetary_db.get(planet, {}).get(house, {})

        rin = rule.get("debt_type")

        if rin:

            rin_report.setdefault(rin, []).append({
                "planet": planet,
                "house": house,
                "risk": rule.get("risk_level", "Low"),
                "karmic_theme": rule.get("karmic_theme", "Unspecified")
            })

    severity = {}

    for rin, items in rin_report.items():
        total = sum(score_map.get(item["risk"], 1) for item in items)
        severity[rin] = total

    return {
        "rin_details": rin_report,
        "rin_severity_score": severity
    }


# ==========================================================
# 🔥 FULL PLANET ACTIVATION (DB DRIVEN)
# ==========================================================

def evaluate_planet_activation(house_map, planetary_db):

    activation_result = {}

    for planet, data in house_map.items():

        house = data.get("house")

        rule = planetary_db.get(planet, {}).get(house, {})

        positive = rule.get("positive_effects", [])
        negative = rule.get("negative_effects", [])
        remedy = rule.get("remedy")
        core_nature = rule.get("core_nature", "General karmic influence")
        karmic_theme = rule.get("karmic_theme", "Life lesson activation")

        # Risk Calculation
        if len(negative) >= 3:
            risk = "High"
        elif len(negative) >= 1:
            risk = "Medium"
        else:
            risk = "Low"

        activation_result[planet] = {
            "house": house,
            "core_nature": core_nature,
            "karmic_theme": karmic_theme,
            "positive_effects": positive,
            "negative_effects": negative,
            "risk_level": risk,
            "suggested_remedy": remedy
        }

    return dict(sorted(activation_result.items()))