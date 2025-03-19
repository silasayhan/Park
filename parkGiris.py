import datetime
from collections import defaultdict
class Oyuncu:
    def __init__(self, ad, yas, odeme_tipi, qr_kod, kart_suresi, giris_tipi="bireysel", kurum_adi=None):
        """
        giris_tipi: "bireysel", "okul", "kuruluş"
        kurum_adi: Eğer giriş tipi "okul" veya "kuruluş" ise buraya okul/şirket adı yazılır.
        """
        self.ad = ad
        self.yas = yas
        self.odeme_tipi = odeme_tipi  # "abonman", "nakit", "günübirlik"
        self.qr_kod = qr_kod
        self.kart_suresi = kart_suresi  # Abonman kart süresi (gün)
        self.giris_tipi = giris_tipi  # "bireysel", "okul", "kuruluş"
        self.kurum_adi = kurum_adi  # Okul veya kuruluş adı

    def kart_dogrula(self):
        """Kartın geçerli olup olmadığını kontrol eder"""
        if self.giris_tipi in ["okul", "kuruluş"]:
            return True  # Okul ve kuruluş girişleri her zaman kabul edilir
        elif self.odeme_tipi == "abonman" and self.kart_suresi > 0:
            return True
        elif self.odeme_tipi in ["nakit", "günübirlik"]:
            return True
        return False

    def kart_uyari(self):
        """Kart süresi azaldığında uyarı verir"""
        if self.odeme_tipi == "abonman" and self.kart_suresi <= 3:
            print(f"⚠️ Uyarı: {self.ad}, abonman süreniz {self.kart_suresi} gün içinde dolacak!")


