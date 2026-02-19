from .1_astronomy_bridge import get_astronomy_data
from .2_house_mapper import map_planets_to_houses
from .3_karmic_engine import (
    evaluate_karmic_structure,
    detect_house_exchange,
    evaluate_debt_cycle,
    evaluate_planet_activation
)
from .4_dosha_engine import (
    evaluate_dosha,
    evaluate_pitru_dosha_lalkitab
)
from .5_remedy_engine import generate_remedies
from .7_risk_engine import calculate_risk

# Lal Kitab Knowledge DB
from services.lalkitab.knowledge.lalkitab_rules import PLANETARY_RULES_DB


class LalKitabAutonomousEngine:

    def __init__(self, birth_data):
        self.birth_data = birth_data

    def generate_kundali(self):

        # STEP 1 — Astronomy Calculation
        planets, lagna = get_astronomy_data(self.birth_data)

        # STEP 2 — Map Planets to Houses
        house_map = map_planets_to_houses(planets)

        # STEP 3 — Core Karmic Structure
        karmic = evaluate_karmic_structure(house_map)

        # STEP 4 — House Exchange Detection
        house_exchange = detect_house_exchange(house_map)

        # STEP 5 — Debt Cycle Evaluation (Rin Logic)
        debt_cycle = evaluate_debt_cycle(
            house_map,
            PLANETARY_RULES_DB
        )

        # STEP 6 — Standard Dosha Engine
        dosha = evaluate_dosha(house_map)

        # STEP 7 — Lal Kitab Pitru Dosha
        pitru_dosha = evaluate_pitru_dosha_lalkitab(house_map)

        # STEP 8 — Remedy Generation
       remedies = generate_remedies(dosha, debt_cycle)

        # STEP 9 — Risk Score Calculation
       risk = calculate_risk(
    karmic,
    dosha,
    debt_cycle,
    pitru_dosha
)

        # FINAL STRUCTURED OUTPUT
        return {
            "Lagna": lagna,
            "Planet_Houses": house_map,
            "Karmic_Flags": karmic,
            "House_Exchange": house_exchange,
            "Debt_Cycle": debt_cycle,
            "Dosha": dosha,
            "Pitru_Dosha": pitru_dosha,
            "Remedies": remedies,
            "Risk_Score": risk
        }