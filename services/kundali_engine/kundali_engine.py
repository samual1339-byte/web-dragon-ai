from datetime import datetime
import traceback

from .scoring_engine import calculate_scores
from ..user_logger.user_logger import log_user_action
from .astronomy_calculator import calculate_planetary_positions
from .planetary_strength import calculate_strength
from .lagna_calculator import calculate_lagna
from .yoga_engine import detect_yogas
from .dosha_engine import detect_doshas
from .interpretation_engine import generate_interpretation
from .kundali_matching_engine import match_kundalis
from ..ai_engine.ai_interpreter import enhance_with_ai
from ..transit_engine.live_transit import get_live_transit


class LalKitabEngine:

    # ======================================================
    # INIT
    # ======================================================

    def __init__(self, birth_data: dict):

        if not isinstance(birth_data, dict):
            raise TypeError("birth_data must be dictionary")

        required_fields = ["date", "time", "place"]
        for field in required_fields:
            if not birth_data.get(field):
                raise ValueError(f"Missing required birth field: {field}")

        self.birth_data = birth_data

    # ======================================================
    # INTERNAL HELPERS
    # ======================================================

    def _structure_planets(self, planet_dict: dict):

        if not isinstance(planet_dict, dict):
            return {"by_planet": {}, "by_house": {}}

        by_planet = planet_dict
        by_house = {}

        for planet, pdata in planet_dict.items():
            house = pdata.get("house")
            if house:
                by_house.setdefault(house, []).append(planet)

        return {
            "by_planet": by_planet,
            "by_house": by_house
        }

    def _safe_transit(self):
        try:
            data = get_live_transit()
            if isinstance(data, dict):
                return data
        except Exception:
            pass
        return {}

    def _normalize_yoga(self, raw, lagna):
        if isinstance(raw, dict):
            return raw.get("yogas", [])
        if isinstance(raw, list):
            return raw
        return []

    def _normalize_dosha(self, raw, lagna):
        if isinstance(raw, dict):
            return raw.get("doshas", [])
        if isinstance(raw, list):
            return raw
        return []

    # ======================================================
    # MAIN GENERATOR
    # ======================================================

    def generate_kundali(self):

        try:

            # --------------------------------------------------
            # 1️⃣ BIRTH PLANETS
            # --------------------------------------------------

            birth_planets_raw = calculate_planetary_positions(self.birth_data)
            birth_planets = self._structure_planets(birth_planets_raw)

            # --------------------------------------------------
            # 2️⃣ LAGNA
            # --------------------------------------------------

            lagna = calculate_lagna(
                self.birth_data.get("name"),
                self.birth_data.get("date"),
                self.birth_data.get("time"),
                self.birth_data.get("place"),
            ) or "Unknown"

            # --------------------------------------------------
            # 3️⃣ PLANET STRENGTH
            # --------------------------------------------------

            strengths = calculate_strength(birth_planets_raw) or {}

            # --------------------------------------------------
            # 4️⃣ YOGA
            # --------------------------------------------------

            raw_yoga = detect_yogas(birth_planets_raw, lagna)
            yogas = self._normalize_yoga(raw_yoga, lagna)

            # --------------------------------------------------
            # 5️⃣ DOSHA
            # --------------------------------------------------

            raw_dosha = detect_doshas(birth_planets_raw, lagna)
            doshas = self._normalize_dosha(raw_dosha, lagna)

            # --------------------------------------------------
            # 6️⃣ SCORING (BIRTH BASED ONLY)
            # --------------------------------------------------

            scores = calculate_scores(
                birth_planets_raw,
                strengths,
                yogas,
                doshas
            ) or {}

            base_destiny_score = scores.get("destiny_score", 60)

            # --------------------------------------------------
            # 7️⃣ CURRENT TRANSIT
            # --------------------------------------------------

            transit_raw = self._safe_transit()
            current_structured = self._structure_planets(transit_raw)

            # --------------------------------------------------
            # 8️⃣ STRUCTURED INTERPRETATION
            # --------------------------------------------------

            interpretation = generate_interpretation(
                birth_planetary_data=birth_planets,
                current_planetary_data=current_structured,
                strengths=strengths,
                yogas=yogas,
                doshas=doshas,
                lagna=lagna,
                name=self.birth_data.get("name", "User")
            )

            # --------------------------------------------------
            # 9️⃣ AI ENHANCEMENT (TEXT ONLY LAYER)
            # --------------------------------------------------

            try:
                ai_boost = enhance_with_ai(
                    interpretation.get("birth_chart", {})
                    .get("personality_summary", "")
                )

                if isinstance(ai_boost, str) and ai_boost.strip():
                    interpretation["ai_analysis"]["enhanced_personality"] = ai_boost

            except Exception:
                pass

            # --------------------------------------------------
            # 🔟 REMEDY EXTRACTION
            # --------------------------------------------------

            remedies = interpretation.get("birth_chart", {}) \
                                     .get("lalkitab", {}) \
                                     .get("remedies", [])

            # --------------------------------------------------
            # 1️⃣1️⃣ LOGGING
            # --------------------------------------------------

            try:
                log_user_action(
                    user=self.birth_data.get("name", "Unknown"),
                    action="Generated Structured Kundali"
                )
            except Exception:
                pass

            # --------------------------------------------------
            # FINAL STRUCTURED RESPONSE
            # --------------------------------------------------

            return {
                "meta": {
                    "generated_at": datetime.utcnow().isoformat(),
                    "engine_version": "2.0-structured"
                },

                "birth_details": self.birth_data,

                "birth_chart": {
                    "lagna": lagna,
                    "planetary_positions": birth_planets,
                    "planetary_strength": strengths,
                    "yogas": yogas,
                    "doshas": doshas,
                    "base_scores": scores
                },

                "current_transit": {
                    "planetary_positions": current_structured
                },

                "interpretation_layers": interpretation,

                "remedies": remedies,

                "final_destiny_score":
                    interpretation.get("ai_analysis", {})
                                  .get("destiny_score", base_destiny_score)
            }

        except Exception as e:
            traceback.print_exc()
            return {
                "error": str(e),
                "generated_at": datetime.utcnow().isoformat()
            }

    # ======================================================
    # MATCHING ENGINE
    # ======================================================

    def generate_kundali_match(self, partner_birth_data: dict):

        try:

            primary_planets = calculate_planetary_positions(self.birth_data) or {}
            partner_planets = calculate_planetary_positions(partner_birth_data) or {}

            primary_strength = calculate_strength(primary_planets) or {}
            partner_strength = calculate_strength(partner_planets) or {}

            match_result = match_kundalis(primary_strength, partner_strength)

            return {
                "matching_result": match_result,
                "generated_at": datetime.utcnow().isoformat()
            }

        except Exception as e:
            traceback.print_exc()
            return {
                "error": str(e),
                "generated_at": datetime.utcnow().isoformat()
            }