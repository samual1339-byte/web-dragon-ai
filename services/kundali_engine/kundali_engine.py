# ==========================================================
# 🔮 KUNDALI ENGINE – CORE MASTER ENGINE (STABILIZED)
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
            if field not in birth_data:
                raise ValueError(f"Missing required birth field: {field}")

        self.birth_data = birth_data

    # ======================================================
    # 🔥 MASTER GENERATION METHOD
    # ======================================================

    def generate_kundali(self):

        try:

            # --------------------------------------------
            # 1️⃣ Calculate Planetary Positions
            # --------------------------------------------
            planets = calculate_planetary_positions(self.birth_data)

            if not isinstance(planets, dict):
                raise ValueError("calculate_planetary_positions must return dict")

            # --------------------------------------------
            # 2️⃣ Calculate Lagna
            # --------------------------------------------
            lagna = calculate_lagna(
                self.birth_data.get("name"),
                self.birth_data.get("date"),
                self.birth_data.get("time"),
                self.birth_data.get("place")
            )

            # --------------------------------------------
            # 3️⃣ Calculate Planetary Strength
            # --------------------------------------------
            strengths = calculate_strength(planets)

            # --------------------------------------------
            # 4️⃣ Detect Yogas
            # --------------------------------------------
            yogas = detect_yogas(planets, lagna)

            # --------------------------------------------
            # 5️⃣ Detect Doshas
            # --------------------------------------------
            doshas = detect_doshas(planets, lagna)

            # --------------------------------------------
            # 6️⃣ Live Transit Data (Safe Wrapper)
            # --------------------------------------------
            try:
                transit_data = get_live_transit()
                if not isinstance(transit_data, dict):
                    transit_data = {}
            except Exception:
                transit_data = {}

            # --------------------------------------------
            # 7️⃣ Generate Interpretation
            # --------------------------------------------
            interpretation = generate_interpretation(
                planets=planets,
                strengths=strengths,
                yogas=yogas,
                doshas=doshas,
                lagna=lagna,
                transit=transit_data
            )

            # --------------------------------------------
            # 8️⃣ AI Enhancement Layer (Safe)
            # --------------------------------------------
            try:
                interpretation = enhance_with_ai(interpretation)
            except Exception:
                pass  # Never break engine due to AI layer

            # --------------------------------------------
            # 9️⃣ Log User Action
            # --------------------------------------------
            try:
                log_user_action(
                    user=self.birth_data.get("name", "Unknown"),
                    action="Generated Kundali"
                )
            except Exception:
                pass  # Logging should never crash engine

            # --------------------------------------------
            # 🔟 FINAL STRUCTURED RETURN
            # --------------------------------------------
            return {
                "birth_data": self.birth_data,
                "planets": planets,
                "lagna": lagna,
                "planetary_strength": strengths,
                "yogas": yogas,
                "doshas": doshas,
                "transit": transit_data,
                "interpretation": interpretation,
                "generated_at": datetime.utcnow().isoformat()
            }

        except Exception as e:
            traceback.print_exc()

            return {
                "birth_data": self.birth_data,
                "error": str(e),
                "generated_at": datetime.utcnow().isoformat()
            }