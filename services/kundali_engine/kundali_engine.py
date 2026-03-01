from datetime import datetime
import traceback

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

    def __init__(self, birth_data: dict):

        if not isinstance(birth_data, dict):
            raise TypeError("birth_data must be dictionary")

        self.birth_data = birth_data


    def _get_safe_transit(self):

        try:
            data = {}
            return data if isinstance(data, dict) else {}
        except Exception:
            return {}
    def generate_kundali(self):

        try:
            planets = calculate_planetary_positions(self.birth_data) or {}
            lagna = calculate_lagna(
                self.birth_data.get("name"),
                self.birth_data.get("date"),
                self.birth_data.get("time"),
                self.birth_data.get("place")
            ) or "Unknown"

            strengths = calculate_strength(planets) or {}
            yogas = detect_yogas(planets, lagna) or []
            doshas = detect_doshas(planets, lagna) or []
            transit_data = self._get_safe_transit()

            interpretation = generate_interpretation(
                planets=planets,
                strengths=strengths,
                yogas=yogas,
                doshas=doshas,
                lagna=lagna,
                transit=transit_data
            ) or ""

            if isinstance(interpretation, dict):
                interpretation = " ".join(str(v) for v in interpretation.values())

            life_interpretation = (
                f"Life influenced by {len(yogas)} yogas and {len(doshas)} doshas."
            )

            remedies = []

            if doshas:
                remedies.extend([
                    "Chant Hanuman Chalisa on Tuesdays.",
                    "Donate black sesame on Saturdays.",
                    "Respect elders and parents.",
                ])

            for planet, pdata in strengths.items():
                if isinstance(pdata, dict):
                    if pdata.get("strength") in ["Weak", "Average"]:
                        remedies.append(
                            f"Strengthen {planet} through mantra and charity."
                        )

            if not remedies:
                remedies.append("No major Lal Kitab remedies required.")

            try:
                interpretation = enhance_with_ai(interpretation)
                if isinstance(interpretation, dict):
                    interpretation = " ".join(str(v) for v in interpretation.values())
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
                "lagna": lagna,
                "planets": planets,
                "planetary_strength": strengths,
                "yogas": yogas,
                "dosha_analysis": {
                    "total_doshas": len(doshas),
                    "doshas": doshas
                },
                "lal_kitab_remedies": remedies,
                "life_interpretation": life_interpretation,
                "detailed_planetary_interpretation": interpretation,
                "transit": transit_data,
                "generated_at": datetime.utcnow().isoformat()
            }

        except Exception as e:
            traceback.print_exc()
            return {
                "error": str(e),
                "generated_at": datetime.utcnow().isoformat()
            }


    def generate_kundali_match(self, partner_birth_data: dict):

        try:
            primary_strength = calculate_strength(
                calculate_planetary_positions(self.birth_data)
            ) or {}

            partner_strength = calculate_strength(
                calculate_planetary_positions(partner_birth_data)
            ) or {}

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