ogrenciler = ["Ali Küçük","Veli Büyük","Mert Günok","Cenk Tosun"]

def ogrenciEkle(ogrAd):
    ogrenciler.extend([ogrAd])
    print(ogrenciler)

def ogrenciSil(ogrAd):
    ogrenciler.remove(ogrAd)
    print(ogrenciler)

def cokluOgrenciEkle(a):
    i = 0
    for i in range (a):
        ogrAd = input("Eklemek istediğiniz öğrencinin adını giriniz:")
        ogrenciler.extend([ogrAd])
        i += 1
    print(ogrenciler)

def yazdir():
    for ogrenci in ogrenciler:
        print(ogrenci)

def ogrenciNumarasiniVer(ogrAd):
    print(ogrenciler.index(ogrAd))

def cokluOgrenciSil(a):
    i = 0
    while i < a:
        ogrAd = input("Silmek istediğiniz öğrenciniz adını giriniz:")
        ogrenciler.remove(ogrAd)
        i += 1
    print(ogrenciler)

ogrenciEkle("Valentin Rosier")
ogrenciSil("Veli Büyük")
cokluOgrenciEkle(5)
cokluOgrenciSil(2)
ogrenciNumarasiniVer("Cenk Tosun")
yazdir()

