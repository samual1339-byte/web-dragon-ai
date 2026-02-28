import copy
import traceback

# ======================================================
# IMPORTS (STABLE & COMPLETE)
# ======================================================

try:
    from services.kundali_engine.lalkitab_autonomous.astronomy_bridge import get_astronomy_data
    from services.kundali_engine.lalkitab_autonomous.house_mapper import map_planets_to_houses
    from services.kundali_engine.lalkitab_autonomous.karmic_engine import (
        evaluate_karmic_structure,
        detect_house_exchange,
        evaluate_debt_cycle,
        evaluate_planet_activation
    )
    from services.kundali_engine.lalkitab_autonomous.dosha_engine import (
        evaluate_dosha,
        evaluate_pitru_dosha_lalkitab
    )
    from services.kundali_engine.lalkitab_autonomous.remedy_engine import generate_remedies
    from services.kundali_engine.lalkitab_autonomous.risk_engine import calculate_risk
    from services.kundali_engine.lalkitab_autonomous.deep_interpretation_engine import generate_deep_interpretation
    from services.kundali_engine.Database.planetary_rule_db import PLANETARY_RULES_DB

except ModuleNotFoundError:
    from .astronomy_bridge import get_astronomy_data
    from .house_mapper import map_planets_to_houses
    from .karmic_engine import (
        evaluate_karmic_structure,
        detect_house_exchange,
        evaluate_debt_cycle,
        evaluate_planet_activation
    )
    from .dosha_engine import (
        evaluate_dosha,
        evaluate_pitru_dosha_lalkitab
    )
    from .remedy_engine import generate_remedies
    from .risk_engine import calculate_risk
    from .deep_interpretation_engine import generate_deep_interpretation
    from ..Database.planetary_rule_db import PLANETARY_RULES_DB


class LalKitabAutonomousEngine:

    def __init__(self, birth_data):
        if not isinstance(birth_data, dict):
            raise TypeError("birth_data must be dictionary.")
        self.birth_data = birth_data

    # ======================================================
    # HOUSE MAP STABILIZER
    # ======================================================

    def _stabilize_house_map(self, house_map):

        if not isinstance(house_map, dict):
            return {}

        stabilized = {}

        for planet, data in house_map.items():
            try:
                safe = copy.deepcopy(data)

                degree = float(safe.get("degree", 0.0))
                degree = round(degree % 360, 2)

                house = int(safe.get("house", 1))
                house = max(1, min(12, house))

                stabilized[planet] = {
                    "rashi": safe.get("rashi"),
                    "degree": degree,
                    "house": house
                }

            except Exception:
                continue

        return dict(sorted(stabilized.items()))

    # ======================================================
    # MAIN ENGINE
    # ======================================================

    def generate_kundali(self):

        try:

            # 1️⃣ Astronomy Layer
            planets, lagna = get_astronomy_data(self.birth_data)

            # 2️⃣ House Mapping
            house_map = map_planets_to_houses(planets)
            house_map = self._stabilize_house_map(house_map)

            # 3️⃣ Karmic Engines
            karmic = evaluate_karmic_structure(house_map)
            house_exchange = detect_house_exchange(house_map)

            debt_cycle = evaluate_debt_cycle(
                house_map,
                PLANETARY_RULES_DB
            )

            planet_activation = evaluate_planet_activation(
                house_map,
                PLANETARY_RULES_DB
            )

            # 4️⃣ Dosha
            dosha = evaluate_dosha(house_map)
            pitru_dosha = evaluate_pitru_dosha_lalkitab(house_map)

            # 5️⃣ Remedies
            remedies = generate_remedies(dosha, debt_cycle)

            # 6️⃣ Risk
            risk = calculate_risk(
                karmic,
                dosha,
                debt_cycle,
                pitru_dosha
            )

            # 7️⃣ Deep Interpretation
            interpretation_text = generate_deep_interpretation(
                planet_activation,
                mode="birth"
            )

            # FINAL RETURN (STABLE)
            return {
                "birth_data": self.birth_data,
                "lagna": lagna,
                "planets": house_map,
                "planetary_insight": planet_activation,
                "doshas": {
                    "primary_dosha": dosha,
                    "pitru_dosha": pitru_dosha
                },
                "remedies": remedies,
                "risk_score": risk.get("risk_score"),
                "risk_level": risk.get("risk_level"),
                "karmic_analysis": karmic,
                "house_exchange": house_exchange,
                "debt_cycle": debt_cycle,
                "interpretation": interpretation_text
            }

        except Exception as e:
            print("ENGINE FAILURE:", str(e))
            traceback.print_exc()
            return {"error": str(e)}