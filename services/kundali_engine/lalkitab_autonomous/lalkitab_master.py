import copy
import datetime

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
    # 🔒 GLOBAL STABILIZATION
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
    # 🔥 PLANETARY INSIGHT LAYER (FIXED EMPTY ISSUE)
    # ======================================================

    def _generate_planetary_insight_layer(self, planet_activation):

        advanced_layer = {}

        if not planet_activation:
            return {}

        # If activation is list → convert to dict
        if isinstance(planet_activation, list):
            activation_dict = {}
            for item in planet_activation:
                planet = item.get("planet")
                if planet:
                    activation_dict[planet] = item
            planet_activation = activation_dict

        for planet, data in planet_activation.items():

            risk_level = data.get("risk_level", "Low")

            risk_weight = 1
            if risk_level == "High":
                risk_weight = 3
            elif risk_level == "Medium":
                risk_weight = 2

            advanced_layer[planet] = {
                "house": data.get("house"),
                "core_nature": data.get("core_nature", "Neutral"),
                "karmic_theme": data.get("karmic_theme", "General karmic influence"),
                "positive_effects": data.get("positive_effects", []),
                "negative_effects": data.get("negative_effects", []),
                "risk_level": risk_level,
                "risk_weight": risk_weight,
                "suggested_remedy": data.get("suggested_remedy", None)
            }

        return dict(sorted(advanced_layer.items()))


    # ======================================================
    # 🪔 REMEDY PRIORITY LAYER
    # ======================================================

    def _generate_remedy_priority(self, remedies, planet_activation):

        priority_score = 0

        if isinstance(planet_activation, list):
            for item in planet_activation:
                level = item.get("risk_level", "Low")
                if level == "High":
                    priority_score += 3
                elif level == "Medium":
                    priority_score += 2
                else:
                    priority_score += 1

        elif isinstance(planet_activation, dict):
            for _, data in planet_activation.items():
                level = data.get("risk_level", "Low")
                if level == "High":
                    priority_score += 3
                elif level == "Medium":
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
    # 🧠 DEEP INTERPRETATION ENGINE (EXPANDED)
    # ======================================================

    def _generate_deep_interpretation(
        self,
        lagna,
        house_map,
        karmic,
        dosha,
        debt_cycle,
        risk
    ):

        interpretation_blocks = []

        interpretation_blocks.append(
            f"Birth Lagna is {lagna}. This defines the psychological core "
            f"and karmic orientation of the native."
        )

        for planet, data in house_map.items():
            house = data.get("house")
            interpretation_blocks.append(
                f"{planet} placed in house {house} influences life themes "
                f"related to that house domain."
            )

        if dosha:
            interpretation_blocks.append(
                f"Detected Doshas: {', '.join(dosha.keys())}."
            )

        if debt_cycle:
            interpretation_blocks.append(
                "Karmic debt cycles indicate unfinished past-life obligations."
            )

        interpretation_blocks.append(
            f"Overall Risk Level calculated as {risk.get('risk_level')} "
            f"with risk score {risk.get('risk_score')}."
        )

        return " ".join(interpretation_blocks)


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

        # IMPORTANT FIX:
        current_age = self.birth_data.get("current_age", 30)

        planet_activation = evaluate_planet_activation(
            current_age,
            {p: d.get("house") for p, d in safe_map.items()}
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

        interpretation = self._generate_deep_interpretation(
            lagna,
            house_map,
            karmic,
            dosha,
            debt_cycle,
            risk
        )

        return {

            "planets": house_map,
            "lagna": lagna,
            "planetary_insight": planetary_insight,
            "doshas": list(dosha.keys()) if isinstance(dosha, dict) else [],
            "risk_score": risk.get("risk_score"),
            "risk_level": risk.get("risk_level"),
            "remedies": remedies,
            "interpretation": interpretation,

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