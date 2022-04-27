import math


def toplama():
    a = int(input("Sayı:"))
    x = n + a
    print("{}".format(n+a))


def uss():
    a = int(input("Sayı:"))
    x = math.pow(n, a)
    print(sonuc)


def bolme():
    a = int(input("Sayı:"))
    x = n / a
    print(x)


def carpma():
    a = int(input("Sayı:"))
    x = n * a
    print(x)


def cikarma():
    a = int(input("Sayı:"))
    x = n - a
    print(x)

def karekok():
    x = math.sqrt(n)
    print("{} sayısının karekökü ={}".format(n,math.sqrt(n)))

n = int(input("Sayı:"))

while True:
    print("""
İşlemler;
    Toplama için +
    Çıkarma için -
    Bölme için /
    Çarpma için x veya *
    Karekökü bulma için k veya K
    Üs almak için ^ veya xy veya XY
            """)
    islem = input("İşlem:")


    if islem == "q":
        print("Hesap Makinesi Kapandı")
        break

    elif islem == "+":
        toplama()
        break

    elif islem == "-":
        cikarma()
        break

    elif islem == "x" or islem == "*":
        carpma()
        break

    elif islem == "/":
        bolme()
        break

    elif islem == "^" or islem == "xy" or islem == "XY":
        a = int(input("Sayı:"))
        sonuc = math.pow(n, a)
        print(sonuc)
        break
    elif islem == "k" or islem == "K":
        karekok()
        break

    else:
        print("Geçersiz tıklama...")
