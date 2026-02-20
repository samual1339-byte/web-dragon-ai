from ..database.guna_matching_db import GUNA_MATCHING_DB
from .manglik_engine import ManglikEvaluator


class LalKitabGunaMatching:

    MAX_SCORE = 36

    def __init__(self, boy_data, girl_data):
        self.boy = boy_data
        self.girl = girl_data

    # -------------------------
    # Individual Guna Methods
    # -------------------------

    def varna(self):
        return self._evaluate_guna("varna")

    def vashya(self):
        return self._evaluate_guna("vashya")

    def tara(self):
        return self._evaluate_guna("tara")

    def yoni(self):
        return self._evaluate_guna("yoni")

    def graha_maitri(self):
        return self._evaluate_guna("graha_maitri")

    def gana(self):
        return self._evaluate_guna("gana")

    def bhakoot(self):
        return self._evaluate_guna("bhakoot")

    def nadi(self):
        return self._evaluate_guna("nadi")

    # -------------------------
    # Core Evaluation Logic
    # -------------------------

    def _evaluate_guna(self, guna_name):

        rule = GUNA_MATCHING_DB.get(guna_name, {})
        max_points = rule.get("points", 0)

        boy_value = self.boy.get(guna_name)
        girl_value = self.girl.get(guna_name)

        # --------------------------------------
        # 1️⃣ VARNA (Hierarchy Based)
        # --------------------------------------
        if guna_name == "varna":
            hierarchy = rule.get("hierarchy", [])
            if boy_value in hierarchy and girl_value in hierarchy:
                if hierarchy.index(boy_value) >= hierarchy.index(girl_value):
                    return max_points
            return 0

        # --------------------------------------
        # 2️⃣ TARA (Nakshatra Distance Based)
        # --------------------------------------
        if guna_name == "tara":
            boy_n = self.boy.get("nakshatra_number")
            girl_n = self.girl.get("nakshatra_number")

            if boy_n and girl_n:
                distance = abs(boy_n - girl_n)
                tara_mod = distance % 9
                favorable = rule.get("favorable_mod", [])
                if tara_mod in favorable:
                    return max_points
            return 0

        # --------------------------------------
        # 3️⃣ BHAKOOT (Rashi Distance Based)
        # --------------------------------------
        if guna_name == "bhakoot":
            boy_rashi = self.boy.get("rashi_number")
            girl_rashi = self.girl.get("rashi_number")

            if boy_rashi and girl_rashi:
                distance = abs(boy_rashi - girl_rashi)
                dosha_distances = rule.get("dosha_distances", [])
                if distance not in dosha_distances:
                    return max_points
            return 0

        # --------------------------------------
        # 4️⃣ NADI (Same = Dosha)
        # --------------------------------------
        if guna_name == "nadi":
            if boy_value and girl_value:
                if boy_value == girl_value:
                    return 0
                return max_points
            return 0

        # --------------------------------------
        # 5️⃣ GRAHA MAITRI (Planetary Friendship)
        # --------------------------------------
        if guna_name == "graha_maitri":
            friendship_map = rule.get("planetary_friendship", {})
            if girl_value in friendship_map.get(boy_value, []):
                return max_points
            return 0

        # --------------------------------------
        # 6️⃣ Default Direct Match Logic
        # --------------------------------------
        if boy_value == girl_value:
            return max_points

        # --------------------------------------
        # 7️⃣ Partial Match Logic (if defined)
        # --------------------------------------
        partial_rules = rule.get("partial_match", {})
        return partial_rules.get((boy_value, girl_value), 0)

    # -------------------------
    # Final Calculation
    # -------------------------

    def calculate_total(self):

        breakdown = {
            "varna": self.varna(),
            "vashya": self.vashya(),
            "tara": self.tara(),
            "yoni": self.yoni(),
            "graha_maitri": self.graha_maitri(),
            "gana": self.gana(),
            "bhakoot": self.bhakoot(),
            "nadi": self.nadi(),
        }

        score = sum(breakdown.values())

        compatibility = (
            "Excellent" if score >= 30 else
            "Very Good" if score >= 24 else
            "Good" if score >= 18 else
            "Average" if score >= 12 else
            "Low"
        )

        # Lal Kitab Special Alerts
        dosha_flags = []

        if breakdown["nadi"] == 0:
            dosha_flags.append("Nadi Dosha")

        if breakdown["bhakoot"] == 0:
            dosha_flags.append("Bhakoot Dosha")

# Manglik Evaluation
manglik_result = None
if self.boy.get("house_map") and self.girl.get("house_map"):
    manglik_result = ManglikEvaluator.evaluate(
        self.boy["house_map"],
        self.girl["house_map"]
    )

 # -------------------------
# Intelligent Enhancements
# -------------------------

# Safe Manglik Handling
manglik_result = None
if self.boy.get("house_map") and self.girl.get("house_map"):
    from .manglik_engine import ManglikEvaluator
    manglik_result = ManglikEvaluator.evaluate(
        self.boy["house_map"],
        self.girl["house_map"]
    )

# AI Marriage Risk
ai_risk = None
if manglik_result:
    from .marriage_risk_ai import MarriageRiskAI
    ai_risk = MarriageRiskAI.evaluate(
        score,
        dosha_flags,
        manglik_result
    )

# Marriage Stability Index
stability = None
if ai_risk:
    from .marriage_stability_engine import MarriageStabilityIndex
    stability = MarriageStabilityIndex.calculate(
        score,
        ai_risk["risk_score"]
    )

# Final Return (Structure Preserved + Enhanced)
return {
    "total_score": score,
    "max_score": self.MAX_SCORE,
    "compatibility": compatibility,
    "guna_breakdown": breakdown,
    "dosha_flags": dosha_flags,

    # ---- New Enhancements ----
    "manglik_analysis": manglik_result,
    "ai_marriage_risk": ai_risk,
    "marriage_stability": stability
}