class OyunAlani:
    def __init__(self, oyuncu):
        self.oyuncu = oyuncu
        self.hiz = self.ozellestir_hiz()
        self.muzik = self.ozellestir_muzik()
        self.sure = self.ozellestir_sure()

    def ozellestir_hiz(self):
        if self.oyuncu.yas < 6:
            return "yavaş"
        elif self.oyuncu.yas < 12:
            return "orta"
        else:
            return "hızlı"

    def ozellestir_muzik(self):
        if self.oyuncu.yas < 6:
            return "çocuk şarkıları"
        elif self.oyuncu.yas < 12:
            return "pop"
        else:
            return "gençlik müzikleri"

    def ozellestir_sure(self):
        return max(10, 30 - self.oyuncu.yas)  # Minimum 10 dakika

    def baslat(self): 
        print(f" {self.oyuncu.ad} için oyun başladı! Hız: {self.hiz}, Müzik: {self.muzik}, Süre: {self.sure} dakika")


class Oyuncu:
    def __init__(self, ad, yas, odeme_tipi, qr_kod, kart_suresi):
        self.ad = ad
        self.yas = yas
        self.odeme_tipi = odeme_tipi
        self.qr_kod = qr_kod
        self.kart_suresi = kart_suresi





