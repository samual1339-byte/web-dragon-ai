class ManglikEvaluator:

    MANGAL_HOUSES = [1, 4, 7, 8, 12]

    @staticmethod
    def is_manglik(house_map):
        mars_house = house_map.get("Mars")
        return mars_house in ManglikEvaluator.MANGAL_HOUSES

    @staticmethod
    def evaluate(boy_house_map, girl_house_map):

        boy_manglik = ManglikEvaluator.is_manglik(boy_house_map)
        girl_manglik = ManglikEvaluator.is_manglik(girl_house_map)

        if boy_manglik and girl_manglik:
            return {
                "status": "Balanced Manglik",
                "risk": "Low"
            }

        if boy_manglik or girl_manglik:
            return {
                "status": "Manglik Mismatch",
                "risk": "High"
            }

        return {
            "status": "No Manglik",
            "risk": "None"
        }