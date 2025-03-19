from collections import defaultdict
import datetime
class Raporlama:
    def __init__(self):
        self.girisler = []
        self.iptaller = 0
        self.satislar = defaultdict(int)
        self.okul_girisleri = defaultdict(int)
        self.kurulus_girisleri = defaultdict(int)

    def giris_ekle(self, oyuncu):
        if oyuncu.kart_dogrula():
            self.girisler.append(oyuncu)
            if oyuncu.odeme_tipi in ["Abonman", "Nakit", "Günübirlik"]:
                self.satislar[oyuncu.odeme_tipi] += 1
            if oyuncu.giris_tipi == "Okul":
                self.okul_girisleri[oyuncu.kurum_adi] += 1
            elif oyuncu.giris_tipi == "Kuruluş":
                self.kurulus_girisleri[oyuncu.kurum_adi] += 1
        else:
            self.iptaller += 1

    def gunluk_rapor(self):
        tarih = datetime.date.today()
        print(f"\nGünlük Rapor ({tarih}):")
        print(f"Toplam Giriş: {len(self.girisler)}")
        print(f"Reddedilen Girişler: {self.iptaller}")
        print("Satışlar:")
        for odeme_tipi, adet in self.satislar.items():
            print(f"   {odeme_tipi}: {adet}")
        print("Okul Girişleri:")
        for okul, adet in self.okul_girisleri.items():
            print(f"   {okul}: {adet}")
        print("Kuruluş Girişleri:")
        for kurulus, adet in self.kurulus_girisleri.items():
            print(f"   {kurulus}: {adet}")

    def haftalik_rapor(self):
        tarih = datetime.date.today()
        baslangic = tarih - datetime.timedelta(days=7)
        print(f"\nHaftalık Rapor ({baslangic} - {tarih}):")
        print(f"Toplam Giriş: {len(self.girisler)}")
        print(f"Reddedilen Girişler: {self.iptaller}")
        print("Satışlar:")
        for odeme_tipi, adet in self.satislar.items():
            print(f"   {odeme_tipi}: {adet}")
        print("Okul Girişleri:")
        for okul, adet in self.okul_girisleri.items():
            print(f"   {okul}: {adet}")
        print("Kuruluş Girişleri:")
        for kurulus, adet in self.kurulus_girisleri.items():
            print(f"   {kurulus}: {adet}")