# ==========================================================
# 🔮 KUNDALI ENGINE – CORE MASTER ENGINE (EXTENDED + STABLE)
# ==========================================================

from datetime import datetime
import traceback

from ..user_logger.user_logger import log_user_action

# SAME FOLDER IMPORTS
from .astronomy_calculator import calculate_planetary_positions
from .planetary_strength import calculate_strength
from .lagna_calculator import calculate_lagna
from .yoga_engine import detect_yogas
from .dosha_engine import detect_doshas
from .interpretation_engine import generate_interpretation
from .kundali_matching_engine import match_kundalis

# SIBLING FOLDER IMPORTS
from ..ai_engine.ai_interpreter import enhance_with_ai
from ..transit_engine.live_transit import get_live_transit


# ==========================================================
# 🔥 MAIN ENGINE CLASS
# ==========================================================

class LalKitabEngine:

    def __init__(self, birth_data: dict):

        if not isinstance(birth_data, dict):
            raise TypeError("birth_data must be a dictionary")

        required_fields = ["date", "time", "place"]

        for field in required_fields:
            if field not in birth_data or not birth_data.get(field):
                raise ValueError(f"Missing required birth field: {field}")

        self.birth_data = birth_data

    # ======================================================
    # 🔥 INTERNAL SAFE TRANSIT WRAPPER
    # ======================================================

    def _get_safe_transit(self):
        try:
            transit_data = get_live_transit()
            if not isinstance(transit_data, dict):
                return {}
            return transit_data
        except Exception:
            return {}

    # ======================================================
    # 🔥 SINGLE KUNDALI GENERATION
    # ======================================================

  def generate_kundali(self):
    try:

        planets = calculate_planetary_positions(self.birth_data)

        if not isinstance(planets, dict):
            raise ValueError("calculate_planetary_positions must return dict")

        lagna = calculate_lagna(
            self.birth_data.get("name"),
            self.birth_data.get("date"),
            self.birth_data.get("time"),
            self.birth_data.get("place")
        )

        strengths = calculate_strength(planets)

        yogas = detect_yogas(planets, lagna)

        doshas = detect_doshas(planets, lagna)

        transit_data = self._get_safe_transit()

        interpretation = generate_interpretation(
            planets=planets,
            strengths=strengths,
            yogas=yogas,
            doshas=doshas,
            lagna=lagna,
            transit=transit_data
        )

        if not interpretation or not interpretation.strip():
            interpretation = (
                f"The native with {lagna} ascendant shows a balanced "
                f"planetary distribution."
            )

        remedies = []

        if "Mangal Dosha" in doshas:
            remedies.extend([
                "Offer red lentils on Tuesday.",
                "Donate red cloth.",
                "Control anger and aggression."
            ])

        if "Kaal Sarp Dosha" in doshas:
            remedies.extend([
                "Offer milk to Shiva on Monday.",
                "Feed stray dogs.",
                "Perform Rahu-Ketu remedies."
            ])

        for planet, data in strengths.items():
            if data.get("strength") == "Average":
                remedies.append(
                    f"Strengthen {planet} through discipline and charity."
                )

        if not remedies:
            remedies.append(
                "No specific remedies suggested. Planetary alignment appears stable."
            )

        try:
            interpretation = enhance_with_ai(interpretation)
        except Exception:
            pass

        try:
            log_user_action(
                user=self.birth_data.get("name", "Unknown"),
                action="Generated Kundali"
            )
        except Exception:
            pass

        return {
            "birth_data": self.birth_data,
            "planets": planets,
            "lagna": lagna,
            "planetary_strength": strengths,
            "yogas": yogas,
            "dosha_analysis": {
                "lagna": lagna,
                "total_doshas": len(doshas),
                "doshas": doshas
            },
            "lal_kitab_remedies": remedies,
            "transit": transit_data,
            "detailed_planetary_interpretation": interpretation,
            "generated_at": datetime.utcnow().isoformat()
        }

    except Exception as e:
        traceback.print_exc()
        return {
            "birth_data": self.birth_data,
            "error": str(e),
            "generated_at": datetime.utcnow().isoformat()
        }
    # ======================================================
    # 💑 KUNDALI MATCHING ENGINE (NEW EXTENSION)
    # ======================================================

    def generate_kundali_match(self, partner_birth_data: dict):

        try:

            if not isinstance(partner_birth_data, dict):
                raise TypeError("partner_birth_data must be dictionary")

            # Generate primary chart
            primary_planets = calculate_planetary_positions(self.birth_data)
            primary_lagna = calculate_lagna(
                self.birth_data.get("name"),
                self.birth_data.get("date"),
                self.birth_data.get("time"),
                self.birth_data.get("place")
            )
            primary_planets = calculate_strength(primary_planets)

            # Generate partner chart
            partner_planets = calculate_planetary_positions(partner_birth_data)
            partner_lagna = calculate_lagna(
                partner_birth_data.get("name"),
                partner_birth_data.get("date"),
                partner_birth_data.get("time"),
                partner_birth_data.get("place")
            )
            partner_planets = calculate_strength(partner_planets)

            # Matching
            matching_result = match_kundalis(
                primary_planets,
                partner_planets
            )

            # Safe Logging
            try:
                log_user_action(
                    user=self.birth_data.get("name", "Unknown"),
                    action="Generated Kundali Matching"
                )
            except Exception:
                pass

            return {
                "primary": {
                    "birth_data": self.birth_data,
                    "lagna": primary_lagna,
                    "planets": primary_planets
                },
                "partner": {
                    "birth_data": partner_birth_data,
                    "lagna": partner_lagna,
                    "planets": partner_planets
                },
                "matching_result": matching_result,
                "generated_at": datetime.utcnow().isoformat()
            }

        except Exception as e:
            traceback.print_exc()

            return {
                "primary_birth_data": self.birth_data,
                "partner_birth_data": partner_birth_data,
                "error": str(e),
                "generated_at": datetime.utcnow().isoformat()
            }