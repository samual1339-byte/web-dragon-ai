class LalKitabGunaMatching:

    MAX_SCORE = 36

    def __init__(self, boy_data, girl_data):
        self.boy = boy_data
        self.girl = girl_data

    def varna(self): return 1
    def vashya(self): return 2
    def tara(self): return 3
    def yoni(self): return 4
    def graha_maitri(self): return 5
    def gana(self): return 6
    def bhakoot(self): return 7
    def nadi(self): return 8

    def calculate_total(self):
        score = (
            self.varna() +
            self.vashya() +
            self.tara() +
            self.yoni() +
            self.graha_maitri() +
            self.gana() +
            self.bhakoot() +
            self.nadi()
        )

        compatibility = (
            "Excellent" if score >= 30 else
            "Very Good" if score >= 24 else
            "Good" if score >= 18 else
            "Average" if score >= 12 else
            "Low"
        )

        return {
            "total_score": score,
            "max_score": self.MAX_SCORE,
            "compatibility": compatibility
        }