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
    # 🔥 PLANETARY INSIGHT LAYER
    # ======================================================

    def _generate_planetary_insight_layer(self, planet_activation):

        advanced_layer = {}

        for planet, data in planet_activation.items():

            risk_weight = 1
            if data.get("risk_level") == "High":
                risk_weight = 3
            elif data.get("risk_level") == "Medium":
                risk_weight = 2

            advanced_layer[planet] = {
                "house": data.get("house"),
                "core_nature": data.get("core_nature"),
                "karmic_theme": data.get("karmic_theme"),
                "positive_effects": data.get("positive_effects", []),
                "negative_effects": data.get("negative_effects", []),
                "risk_level": data.get("risk_level"),
                "risk_weight": risk_weight,
                "suggested_remedy": data.get("suggested_remedy")
            }

        return dict(sorted(advanced_layer.items()))

    # ======================================================
    # 🪔 REMEDY PRIORITY LAYER
    # ======================================================

    def _generate_remedy_priority(self, remedies, planet_activation):

        priority_score = 0

        for _, data in planet_activation.items():
            if data.get("risk_level") == "High":
                priority_score += 3
            elif data.get("risk_level") == "Medium":
                priority_score += 2
            else:
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
    # 🔮 MAIN ENGINE
    # ======================================================

    def generate_kundali(self):

        planets, lagna = get_astronomy_data(self.birth_data)

        raw_house_map = map_planets_to_houses(planets)

        house_map = self._stabilize_house_map(raw_house_map)

        safe_map = copy.deepcopy(house_map)

        karmic = evaluate_karmic_structure(copy.deepcopy(safe_map))

        house_exchange = detect_house_exchange(copy.deepcopy(safe_map))

        debt_cycle = evaluate_debt_cycle(
            copy.deepcopy(safe_map),
            PLANETARY_RULES_DB
        )

        planet_activation = evaluate_planet_activation(
            copy.deepcopy(safe_map),
            PLANETARY_RULES_DB
        )

        planetary_insight = self._generate_planetary_insight_layer(
            planet_activation
        )

        dosha = evaluate_dosha(copy.deepcopy(safe_map))

        pitru_dosha = evaluate_pitru_dosha_lalkitab(
            copy.deepcopy(safe_map)
        )

        remedies = generate_remedies(
            dosha or {},
            debt_cycle or {}
        )

        remedy_priority = self._generate_remedy_priority(
            remedies,
            planet_activation
        )

        risk = calculate_risk(
            karmic or {},
            dosha or {},
            debt_cycle or {},
            pitru_dosha or {}
        )

        # ======================================================
        # 🧠 SIMPLE AUTO INTERPRETATION GENERATOR
        # ======================================================

        interpretation = (
            f"Lagna in {lagna}. "
            f"Overall Risk Level: {risk.get('risk_level')}. "
            f"Remedy Priority: {remedy_priority.get('priority_label')}."
        )

        # ======================================================
        # ✅ FINAL OUTPUT (UI COMPATIBLE + STRUCTURED)
        # ======================================================

        return {

            # ===== UI Compatible Keys =====
            "planets": house_map,
            "lagna": lagna,
            "planetary_insight": planetary_insight,
            "doshas": list(dosha.keys()) if isinstance(dosha, dict) else [],
            "risk_score": risk.get("risk_score"),
            "risk_level": risk.get("risk_level"),
            "remedies": remedies,
            "interpretation": interpretation,

            # ===== Advanced Structured Blocks =====
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