import datetime

class Muhasebe:
    def __init__(self):
        self.gelirler = []  # (tarih, miktar, aciklama)
        self.giderler = []  # (tarih, miktar, aciklama)

    def gelir_ekle(self, miktar, aciklama=""):
        """Yeni bir gelir ekler."""
        self.gelirler.append((datetime.date.today(), miktar, aciklama))
        print(f"✅ {miktar} TL gelir eklendi: {aciklama}")

    def gider_ekle(self, miktar, aciklama=""):
        """Yeni bir gider ekler."""
        self.giderler.append((datetime.date.today(), miktar, aciklama))
        print(f"❌ {miktar} TL gider eklendi: {aciklama}")

    def toplam_gelir(self):
        """Toplam geliri hesaplar."""
        return sum(gelir[1] for gelir in self.gelirler)

    def toplam_gider(self):
        """Toplam gideri hesaplar."""
        return sum(gider[1] for gider in self.giderler)

    def kar_zarar_hesapla(self):
        """Kar veya zarar durumunu hesaplar."""
        kar_zarar = self.toplam_gelir() - self.toplam_gider()
        durum = "Kâr" if kar_zarar >= 0 else "Zarar"
        print(f"{durum} Durumu: {kar_zarar} TL")
        return kar_zarar

    def rapor_al(self):
        """Gelir ve giderleri detaylı rapor olarak döndürür."""
        print("\nMuhasebe Raporu")
        print("------------------")
        print("Gelirler:")
        for gelir in self.gelirler:
            print(f"{gelir[0]} - {gelir[1]} TL: {gelir[2]}")
        print("\nGiderler:")
        for gider in self.giderler:
            print(f"{gider[0]} - {gider[1]} TL: {gider[2]}")
        self.kar_zarar_hesapla()

# ------------------------- TESTLER -------------------------

def test_muhasebe():
    muhasebe = Muhasebe()
    
    muhasebe.gelir_ekle(5000, "Bilet Satısları")
    muhasebe.gelir_ekle(2000, "Kafeterya Satısları")
    muhasebe.gider_ekle(3000, "Personel Maasları")
    muhasebe.gider_ekle(1000, "Bakım Masrafları")
    
    assert muhasebe.toplam_gelir() == 7000
    assert muhasebe.toplam_gider() == 4000
    assert muhasebe.kar_zarar_hesapla() == 3000
    
    muhasebe.rapor_al()
    print("\n✅ Muhasebe Testleri Basarili!")

if __name__ == "__main__":
    test_muhasebe()
