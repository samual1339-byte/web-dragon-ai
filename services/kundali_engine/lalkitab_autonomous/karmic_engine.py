class AdvancedKarmicLogic:

    def __init__(self, kundali, planetary_db):
        self.kundali = kundali
        self.db = planetary_db

    # ===============================
    # HOUSE EXCHANGE LOGIC
    # ===============================

    def detect_house_exchange(self):
        exchanges = []

        for p1, h1 in self.kundali.items():
            for p2, h2 in self.kundali.items():
                if p1 != p2:
                    if h1 == self.kundali.get(p2) and h2 == self.kundali.get(p1):
                        exchanges.append({
                            "planet_1": p1,
                            "planet_2": p2,
                            "type": "Direct Exchange"
                        })

        return exchanges

    # ===============================
    # DEBT CYCLE LOGIC
    # ===============================

    def evaluate_debt_cycle(self):
        rin_report = {}
        score_map = {"Low": 1, "Medium": 2, "High": 3}

        for planet, house in self.kundali.items():
            rule = self.db.get(planet, {}).get(house, {})
            rin = rule.get("debt_type")

            if rin:
                rin_report.setdefault(rin, []).append({
                    "planet": planet,
                    "house": house,
                    "risk": rule.get("risk_level"),
                    "karmic_theme": rule.get("karmic_theme")
                })

        severity = {}
        for rin, items in rin_report.items():
            total = sum(score_map.get(item["risk"], 1) for item in items)
            severity[rin] = total

        return {
            "rin_details": rin_report,
            "rin_severity_score": severity
        }

def detect_house_exchange(house_map):
    exchanges = []

    for p1, h1 in house_map.items():
        for p2, h2 in house_map.items():
            if p1 != p2:
                if h1 == house_map.get(p2) and h2 == house_map.get(p1):
                    exchanges.append({
                        "planet_1": p1,
                        "planet_2": p2,
                        "type": "Direct Exchange"
                    })

    return exchanges


def evaluate_debt_cycle(house_map, planetary_db):

    rin_report = {}
    score_map = {"Low": 1, "Medium": 2, "High": 3}

    for planet, house in house_map.items():
        rule = planetary_db.get(planet, {}).get(house, {})
        rin = rule.get("debt_type")

        if rin:
            rin_report.setdefault(rin, []).append({
                "planet": planet,
                "house": house,
                "risk": rule.get("risk_level"),
                "karmic_theme": rule.get("karmic_theme")
            })

    severity = {}
    for rin, items in rin_report.items():
        total = sum(score_map.get(item["risk"], 1) for item in items)
        severity[rin] = total

    return {
        "rin_details": rin_report,
        "rin_severity_score": severity
    }
PLANET_MATURITY_AGE = {
    "Sun": 22,
    "Moon": 24,
    "Mars": 28,
    "Mercury": 32,
    "Jupiter": 16,
    "Venus": 25,
    "Saturn": 36,
    "Rahu": 42,
    "Ketu": 48
}

def evaluate_planet_activation(current_age, house_map):

    activated = []

    for planet, age in PLANET_MATURITY_AGE.items():
        if current_age >= age and planet in house_map:
            activated.append({
                "planet": planet,
                "house": house_map[planet],
                "activation_age": age
            })

    return activated