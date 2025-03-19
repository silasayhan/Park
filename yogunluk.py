import random
from collections import defaultdict

class YogunlukTahmin:
    def __init__(self, raporlama):
        self.raporlama = raporlama
    
    def tahmin_et(self, gun):
        son_girisler = [len(self.raporlama.girisler) - i for i in range(min(5, len(self.raporlama.girisler)))]
        if not son_girisler:
            return 0
        ortalama = sum(son_girisler) / len(son_girisler)
        varyasyon = random.uniform(0.9, 1.1)  # %10 rastgele varyasyon
        return int(ortalama * varyasyon)