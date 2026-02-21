class ManglikEvaluator:

    MANGAL_HOUSES = (1, 4, 7, 8, 12)

    @staticmethod
    def _extract_mars_house(house_map):
        """
        Safely extract Mars house from structured house_map.
        Deterministic and type-safe.
        """

        if not isinstance(house_map, dict):
            return None

        mars_data = house_map.get("Mars")

        if not mars_data:
            return None

        if isinstance(mars_data, dict):
            return int(mars_data.get("house", 0))

        # Backward compatibility (if old structure passed)
        return int(mars_data)

    @staticmethod
    def is_manglik(house_map):
        """
        Stable Manglik detection.
        """

        mars_house = ManglikEvaluator._extract_mars_house(house_map)

        if mars_house is None:
            return False

        return mars_house in ManglikEvaluator.MANGAL_HOUSES

    @staticmethod
    def evaluate(boy_house_map, girl_house_map):
        """
        Deterministic Manglik compatibility evaluation.
        Fully structured output.
        """

        boy_mars_house = ManglikEvaluator._extract_mars_house(boy_house_map)
        girl_mars_house = ManglikEvaluator._extract_mars_house(girl_house_map)

        boy_manglik = boy_mars_house in ManglikEvaluator.MANGAL_HOUSES
        girl_manglik = girl_mars_house in ManglikEvaluator.MANGAL_HOUSES

        if boy_manglik and girl_manglik:
            return {
                "status": "Balanced Manglik",
                "risk": "Low",
                "boy_mars_house": boy_mars_house,
                "girl_mars_house": girl_mars_house,
                "boy_manglik": True,
                "girl_manglik": True
            }

        if boy_manglik or girl_manglik:
            return {
                "status": "Manglik Mismatch",
                "risk": "High",
                "boy_mars_house": boy_mars_house,
                "girl_mars_house": girl_mars_house,
                "boy_manglik": boy_manglik,
                "girl_manglik": girl_manglik
            }

        return {
            "status": "No Manglik",
            "risk": "None",
            "boy_mars_house": boy_mars_house,
            "girl_mars_house": girl_mars_house,
            "boy_manglik": False,
            "girl_manglik": False
        }