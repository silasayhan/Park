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


def test_oyun_alani():
    print("\nOyun Alanı Testleri Başlıyor...\n")

    # 1️⃣ Küçük çocuk (yaş: 5)
    oyuncu1 = Oyuncu("Mete", 5, "abonman", "QR999", 10)
    oyun1 = OyunAlani(oyuncu1)
    assert oyun1.hiz == "yavaş"
    assert oyun1.muzik == "çocuk şarkıları"
    assert oyun1.sure == 25  # 30 - 5 = 25 dk
    print(f" Test 1 - {oyuncu1.ad}: Hız: {oyun1.hiz}, Müzik: {oyun1.muzik}, Süre: {oyun1.sure} dk")

    # 2️⃣ Orta yaş grubu (yaş: 10)
    oyuncu2 = Oyuncu("Ela", 10, "günübirlik", "QR222", None)
    oyun2 = OyunAlani(oyuncu2)
    assert oyun2.hiz == "orta"
    assert oyun2.muzik == "pop"
    assert oyun2.sure == 20  # 30 - 10 = 20 dk
    print(f" Test 2 - {oyuncu2.ad}: Hız: {oyun2.hiz}, Müzik: {oyun2.muzik}, Süre: {oyun2.sure} dk")

    # 3️⃣ Büyük yaş grubu (yaş: 15)
    oyuncu3 = Oyuncu("Berk", 15, "nakit", "QR333", None)
    oyun3 = OyunAlani(oyuncu3)
    assert oyun3.hiz == "hızlı"
    assert oyun3.muzik == "gençlik müzikleri"
    assert oyun3.sure == 15  # 30 - 15 = 15 dk
    print(f" Test 3 - {oyuncu3.ad}: Hiz: {oyun3.hiz}, Müzik: {oyun3.muzik}, Süre: {oyun3.sure} dk")

    print("\n Oyun Alanı testleri tamamlandı!\n")


if __name__ == "__main__":
    test_oyun_alani()

