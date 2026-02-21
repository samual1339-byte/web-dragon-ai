import copy

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

from ..database.planetary_rule_db import PLANETARY_RULES_DB


class LalKitabAutonomousEngine:

    def __init__(self, birth_data):
        if not isinstance(birth_data, dict):
            raise TypeError("birth_data must be dictionary.")
        self.birth_data = birth_data

    # ======================================================
    # 🔒 GLOBAL STABILIZATION LAYER
    # ======================================================

    def _stabilize_house_map(self, house_map):
        """
        Hard lock:
        - Degree normalization (0–360)
        - 2 decimal precision
        - House as integer
        - Deterministic ordering
        - No mutation side effects
        """

        stabilized = {}

        for planet, data in house_map.items():

            safe_data = copy.deepcopy(data)

            degree = float(safe_data.get("degree", 0.0))
            degree = round(degree % 360, 2)

            house = int(safe_data.get("house", 0))

            safe_data["degree"] = degree
            safe_data["house"] = house

            stabilized[planet] = safe_data

        return dict(sorted(stabilized.items()))

    # ======================================================
    # 🔥 INTERNAL ENHANCEMENT LAYER
    # ======================================================

    def _generate_planetary_insight_layer(self, planet_activation):

        advanced_layer = {}

        for planet, data in planet_activation.items():

            risk_weight = 0

            if data.get("risk_level") == "High":
                risk_weight = 3
            elif data.get("risk_level") == "Medium":
                risk_weight = 2
            elif data.get("risk_level") == "Low":
                risk_weight = 1

            advanced_layer[planet] = {
                "house": data.get("house"),
                "core_nature": data.get("core_nature"),
                "karmic_theme": data.get("karmic_theme"),
                "positive_effects": data.get("positive_effects", []),
                "negative_effects": data.get("negative_effects", []),
                "hidden_effect": data.get("hidden_effect"),
                "debt_type": data.get("debt_type"),
                "risk_level": data.get("risk_level"),
                "risk_weight": risk_weight,
                "special_notes": data.get("special_notes", [])
            }

        return dict(sorted(advanced_layer.items()))

    def _generate_remedy_priority(self, remedies, planet_activation):

        priority_score = 0

        for _, data in planet_activation.items():
            if data.get("risk_level") == "High":
                priority_score += 3
            elif data.get("risk_level") == "Medium":
                priority_score += 2
            elif data.get("risk_level") == "Low":
                priority_score += 1

        if priority_score >= 20:
            priority_label = "Critical"
        elif priority_score >= 12:
            priority_label = "High"
        elif priority_score >= 6:
            priority_label = "Moderate"
        else:
            priority_label = "Routine"

        return {
            "priority_score": priority_score,
            "priority_label": priority_label,
            "recommended_remedies": remedies or []
        }

    # ======================================================
    # 🔮 MAIN ENGINE (FULLY DETERMINISTIC)
    # ======================================================

    def generate_kundali(self):

        # ----------------------------------------
        # STEP 1 — Astronomy Calculation
        # ----------------------------------------
        planets, lagna = get_astronomy_data(self.birth_data)

        # ----------------------------------------
        # STEP 2 — Map Planets to Houses
        # ----------------------------------------
        raw_house_map = map_planets_to_houses(planets)

        # ----------------------------------------
        # 🔒 STABILIZATION APPLIED HERE
        # ----------------------------------------
        house_map = self._stabilize_house_map(raw_house_map)

        # Deep copy for safety (no mutation by engines)
        safe_house_map = copy.deepcopy(house_map)

        # ----------------------------------------
        # STEP 3 — Core Karmic Structure
        # ----------------------------------------
        karmic = evaluate_karmic_structure(copy.deepcopy(safe_house_map))

        # ----------------------------------------
        # STEP 4 — House Exchange Detection
        # ----------------------------------------
        house_exchange = detect_house_exchange(copy.deepcopy(safe_house_map))

        # ----------------------------------------
        # STEP 5 — Debt Cycle Evaluation
        # ----------------------------------------
        debt_cycle = evaluate_debt_cycle(
            copy.deepcopy(safe_house_map),
            PLANETARY_RULES_DB
        )

        # ----------------------------------------
        # STEP 6 — Planet Activation Layer
        # ----------------------------------------
        planet_activation = evaluate_planet_activation(
            copy.deepcopy(safe_house_map),
            PLANETARY_RULES_DB
        )

        # ----------------------------------------
        # STEP 7 — Deep Insight Enhancement
        # ----------------------------------------
        planetary_insight = self._generate_planetary_insight_layer(
            planet_activation
        )

        # ----------------------------------------
        # STEP 8 — Dosha Engine
        # ----------------------------------------
        dosha = evaluate_dosha(copy.deepcopy(safe_house_map))

        # ----------------------------------------
        # STEP 9 — Pitru Dosha
        # ----------------------------------------
        pitru_dosha = evaluate_pitru_dosha_lalkitab(
            copy.deepcopy(safe_house_map)
        )

        # ----------------------------------------
        # STEP 10 — Remedy Generation
        # ----------------------------------------
        remedies = generate_remedies(
            dosha or {},
            debt_cycle or {}
        )

        # ----------------------------------------
        # STEP 11 — Remedy Priority Intelligence
        # ----------------------------------------
        remedy_priority = self._generate_remedy_priority(
            remedies,
            planet_activation
        )

        # ----------------------------------------
        # STEP 12 — Risk Score
        # ----------------------------------------
        risk = calculate_risk(
            karmic or {},
            dosha or {},
            debt_cycle or {},
            pitru_dosha or {}
        )

        # ----------------------------------------
        # FINAL OUTPUT (STABLE & ORDERED)
        # ----------------------------------------
        return {
            "Lagna": lagna,
            "Planet_Houses": house_map,
            "Karmic_Flags": karmic,
            "House_Exchange": house_exchange,
            "Debt_Cycle": debt_cycle,
            "Planet_Activation": planet_activation,
            "Planetary_Insight": planetary_insight,
            "Dosha": dosha,
            "Pitru_Dosha": pitru_dosha,
            "Remedies": remedies,
            "Remedy_Priority": remedy_priority,
            "Risk_Score": risk
        }