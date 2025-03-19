from abc import ABC, abstractmethod
from datetime import datetime, timedelta

# Personel Arayüzü
class Personel(ABC):
    def __init__(self, ad, soyad, pozisyon):
        self.ad = ad
        self.soyad = soyad
        self.pozisyon = pozisyon
    
    @abstractmethod
    def bilgileri_goster(self):
        pass

# Müşteri Destek & Oyun Alanı Bakım
class MusteriDestek(Personel):
    def __init__(self, ad, soyad):
        super().__init__(ad, soyad, "Müşteri Destek")
    
    def bilgileri_goster(self):
        return f"{self.ad} {self.soyad} - {self.pozisyon}"

class OyunAlaniBakim(Personel):  # Reyon Bakım yerine Oyun Alanı Bakımı
    def __init__(self, ad, soyad):
        super().__init__(ad, soyad, "Oyun Alanı Bakımı")
    
    def bilgileri_goster(self):
        return f"{self.ad} {self.soyad} - {self.pozisyon}"

# Stok İşlemleri Yönetimi
class StokYonetim:
    def __init__(self):
        self.stoklar = {}
    
    def urun_ekle(self, urun, miktar):
        if urun in self.stoklar:
            self.stoklar[urun] += miktar
        else:
            self.stoklar[urun] = miktar
    
    def urun_cikar(self, urun, miktar):
        if urun in self.stoklar and self.stoklar[urun] >= miktar:
            self.stoklar[urun] -= miktar
    
    def stok_durumu(self):
        return self.stoklar

# Nöbet Çizelgesi & İzin Yönetimi
class NobetCizelgesi:
    def __init__(self):
        self.nobet_listesi = {}
    
    def nobet_ekle(self, personel, tarih):
        self.nobet_listesi[tarih] = personel.bilgileri_goster()
    
    def nobetleri_goster(self):
        return self.nobet_listesi

class IzinYonetimi:
    def __init__(self):
        self.izinler = {}
    
    def izin_talep_et(self, personel, tarih):
        self.izinler[tarih] = personel.bilgileri_goster()
    
    def izin_listesi(self):
        return self.izinler

# Maaş & Prim Talepleri
class MaasPrimYonetimi:
    def __init__(self):
        self.maas_prim = {}
    
    def maas_ayarla(self, personel, maas):
        self.maas_prim[personel.bilgileri_goster()] = {"Maas": maas, "Prim": 0}
    
    def prim_ekle(self, personel, prim):
        if personel.bilgileri_goster() in self.maas_prim:
            self.maas_prim[personel.bilgileri_goster()]["Prim"] += prim
    
    def maas_ve_prim_goster(self):
        return self.maas_prim

