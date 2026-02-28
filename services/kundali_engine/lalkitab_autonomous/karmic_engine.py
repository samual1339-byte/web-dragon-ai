import copy


# ==========================================================
# 🔥 INTERNAL SAFE HELPERS
# ==========================================================

def _safe_get_house(data):
    if not isinstance(data, dict):
        return None
    return data.get("house")


def _safe_get_planet_rules(planetary_db, planet):
    if not isinstance(planetary_db, dict):
        return {}
    planet_block = planetary_db.get(planet, {})
    if not isinstance(planet_block, dict):
        return {}
    return planet_block.get("house_rules", {})


def _safe_get_rule(planet_rules, house):
    if not isinstance(planet_rules, dict):
        return {}
    return (
        planet_rules.get(house)
        or planet_rules.get(str(house))
        or {}
    )


# ==========================================================
# 🔥 KARMIC STRUCTURE EVALUATION
# ==========================================================

def evaluate_karmic_structure(house_map):

    karmic_flags = {}

    if not isinstance(house_map, dict):
        return {}

    for planet, data in house_map.items():

        house = _safe_get_house(data)
        if house is None:
            continue

        if house in [6, 8, 12]:
            intensity = "High"
            theme = "Past life unresolved karma"
            weight = 3

        elif house in [1, 5, 9]:
            intensity = "Positive"
            theme = "Dharma activation"
            weight = 1

        else:
            intensity = "Neutral"
            theme = "Material life experience"
            weight = 2

        karmic_flags[planet] = {
            "house": house,
            "karmic_intensity": intensity,
            "karmic_weight": weight,
            "theme": theme
        }

    return dict(sorted(karmic_flags.items()))


# ==========================================================
# 🔁 HOUSE EXCHANGE LOGIC (Improved Real Exchange Detection)
# ==========================================================

def detect_house_exchange(house_map):

    exchanges = []

    if not isinstance(house_map, dict):
        return []

    planets = list(house_map.keys())

    for i in range(len(planets)):
        for j in range(i + 1, len(planets)):

            p1 = planets[i]
            p2 = planets[j]

            h1 = _safe_get_house(house_map.get(p1))
            h2 = _safe_get_house(house_map.get(p2))

            if h1 is None or h2 is None:
                continue

            # Direct same-house conjunction
            if h1 == h2:
                exchanges.append({
                    "planet_1": p1,
                    "planet_2": p2,
                    "type": "Conjunction",
                    "house": h1
                })

    return exchanges


# ==========================================================
# 💰 DEBT CYCLE (RIN LOGIC) – DB STRUCTURE AWARE
# ==========================================================

def evaluate_debt_cycle(house_map, planetary_db):

    rin_report = {}
    score_map = {"Low": 1, "Medium": 2, "High": 3}

    if not isinstance(house_map, dict):
        return {}

    if not isinstance(planetary_db, dict):
        return {}

    for planet, data in house_map.items():

        house = _safe_get_house(data)
        if house is None:
            continue

        planet_rules = _safe_get_planet_rules(planetary_db, planet)
        rule = _safe_get_rule(planet_rules, house)

        if not isinstance(rule, dict):
            continue

        rin = rule.get("debt_type")
        if not rin:
            continue

        rin_report.setdefault(rin, []).append({
            "planet": planet,
            "house": house,
            "risk": rule.get("risk_level", "Low"),
            "severity_weight": rule.get("severity_weight", score_map.get(rule.get("risk_level", "Low"), 1)),
            "karmic_theme": rule.get("karmic_theme", "Unspecified")
        })

    severity = {}

    for rin, items in rin_report.items():
        total = sum(item.get("severity_weight", 1) for item in items)
        severity[rin] = {
            "total_score": total,
            "intensity":
                "High" if total >= 6 else
                "Medium" if total >= 3 else
                "Low"
        }

    return {
        "rin_details": rin_report,
        "rin_severity_score": severity
    }


# ==========================================================
# 🔥 FULL PLANET ACTIVATION (DB STRUCTURE v2 READY)
# ==========================================================

def evaluate_planet_activation(house_map, planetary_db):

    activation_result = {}

    if not isinstance(house_map, dict):
        return {}

    for planet, data in house_map.items():

        house = _safe_get_house(data)
        if house is None:
            continue

        planet_block = planetary_db.get(planet, {})
        planet_meta = planet_block.get("planet_meta", {})
        planet_rules = planet_block.get("house_rules", {})

        rule = _safe_get_rule(planet_rules, house)

        if not isinstance(rule, dict):
            continue

        positive = rule.get("positive_effects", [])
        negative = rule.get("negative_effects", [])

        risk = rule.get("risk_level")
        if not risk:
            if len(negative) >= 3:
                risk = "High"
            elif len(negative) >= 1:
                risk = "Medium"
            else:
                risk = "Low"

        activation_result[planet] = {
            "house": house,
            "planet_category": planet_meta.get("category"),
            "element": planet_meta.get("element"),
            "core_nature": rule.get("core_nature", "General karmic influence"),
            "karmic_theme": rule.get("karmic_theme", "Life lesson activation"),
            "positive_effects": positive,
            "negative_effects": negative,
            "risk_level": risk,
            "severity_weight": rule.get("severity_weight", 1),
            "activates_house": rule.get("activates_house"),
            "hidden_effect": rule.get("hidden_effect"),
            "suggested_remedy": rule.get("remedy"),
        }

    return dict(sorted(activation_result.items()))