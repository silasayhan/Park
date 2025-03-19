import datetime

# ------------------------- OYUNCU SINIFI -------------------------

class Oyuncu:
    def __init__(self, ad, yas, odeme_tipi, qr_kod, kart_suresi, giris_tipi="bireysel", kurum_adi=None):
        """
        giris_tipi: "bireysel", "okul", "kuruluş"
        kurum_adi: Eğer giriş tipi "okul" veya "kuruluş" ise buraya okul/şirket adı yazılır.
        """
        self.ad = ad
        self.yas = yas
        self.odeme_tipi = odeme_tipi
        self.qr_kod = qr_kod
        self.kart_suresi = kart_suresi
        self.giris_tipi = giris_tipi  # "bireysel", "okul", "kuruluş"
        self.kurum_adi = kurum_adi  # Okul veya kuruluş adı

    def kart_dogrula(self):
        if self.giris_tipi in ["okul", "kuruluş"]:
            return True  # Okul ve kuruluş girişleri her zaman kabul edilir
        elif self.odeme_tipi == "abonman" and self.kart_suresi > 0:
            return True
        elif self.odeme_tipi in ["nakit", "günübirlik"]:
            return True
        return False

    def kart_uyari(self):
        if self.odeme_tipi == "abonman" and self.kart_suresi is not None and self.kart_suresi <= 3:
            print(f"⚠️ Uyarı: {self.ad}, abonman süreniz {self.kart_suresi} gün içinde dolacak!")

# ------------------------- TESTLER -------------------------

def test_giris():
    print("\n Giriş Testleri Başlıyor...\n")

    oyuncu1 = Oyuncu("Ali", 8, "abonman", "QR123", 5)
    assert oyuncu1.kart_dogrula() == True
    print(f"✅ Test 1 - {oyuncu1.ad} için abonman kartı doğrulandı.")

    oyuncu2 = Oyuncu("Veli", 10, "abonman", "QR456", 0)
    assert oyuncu2.kart_dogrula() == False
    print(f"❌ Test 2 - {oyuncu2.ad} için abonman süresi dolmuş, giriş reddedildi.")

    oyuncu3 = Oyuncu("Ahmet", 12, "nakit", "QR789", None)
    assert oyuncu3.kart_dogrula() == True
    print(f"✅ Test 3 - {oyuncu3.ad} için nakit ödeme kabul edildi.")

    oyuncu4 = Oyuncu("Zeynep", 5, "günübirlik", "QR321", None)
    assert oyuncu4.kart_dogrula() == True
    print(f"✅ Test 4 - {oyuncu4.ad} günübirlik giriş yaptı.")

    oyuncu5 = Oyuncu("Ece", 9, "abonman", "QR654", 2)
    print(f"⚠ Test 5 - {oyuncu5.ad} için hatırlatma mesajı bekleniyor...")
    oyuncu5.kart_uyari()

    oyuncu6 = Oyuncu("Mehmet", 10, "okul", "QR999", None, giris_tipi="okul", kurum_adi="Atatürk Ortaokulu")
    assert oyuncu6.kart_dogrula() == True
    print(f"✅Test 6 - {oyuncu6.ad} ({oyuncu6.kurum_adi}) okul giriş yaptı.")

    oyuncu7 = Oyuncu("Elif", 30, "kuruluş", "QR777", None, giris_tipi="kuruluş", kurum_adi="Teknopark AŞ")
    assert oyuncu7.kart_dogrula() == True
    print(f"✅Test 7 - {oyuncu7.ad} ({oyuncu7.kurum_adi}) şirket giriş yaptı.")

    print("\n✅ Giriş testleri tamamlandı!\n")

def test_oyun_alani():
    print("\n Oyun Alanı Testleri Başlıyor...\n")

    oyuncu1 = Oyuncu("Mete", 5, "abonman", "QR999", 10)
    assert oyuncu1.kart_dogrula() == True
    print(f"✅ Test 1 - {oyuncu1.ad} için oyun alanına giriş doğrulandı.")

    oyuncu2 = Oyuncu("Ela", 10, "günübirlik", "QR222", None)
    assert oyuncu2.kart_dogrula() == True
    print(f"✅ Test 2 - {oyuncu2.ad} için oyun alanına giriş doğrulandı.")

    print("\n✅ Oyun Alanı testleri tamamlandı!\n")

def test_muhasebe():
    print("\n Muhasebe Testleri Başlıyor...\n")

    muhasebe = {"gelir": 5000, "gider": 2000}
    
    assert muhasebe["gelir"] == 5000
    assert muhasebe["gider"] == 2000
    assert (muhasebe["gelir"] - muhasebe["gider"]) == 3000
    
    print("\n✅ Muhasebe Testleri Başarılı!")

def test_personel():
    print("\n Personel Testleri Başlıyor...\n")

    personel1 = {"ad": "Ahmet", "gorev": "Müşteri Destek"}
    assert personel1["gorev"] == "Müşteri Destek"
    print(f"✅ Test 1 - {personel1['ad']} ({personel1['gorev']}) doğru atandı.")

    print("\n✅ Personel Testleri Tamamlandı!\n")

# ------------------------- TESTLERİ ÇALIŞTIR -------------------------

if __name__ == "__main__":
    test_giris()
    test_oyun_alani()
    test_muhasebe()
    test_personel()
