import time

programs = ["Explorer"]

class bilgisayar():
    def __init__(self,pc_durum = "Kapalı",pc_oturum = "User",pc_pass = "none",programlar = programs,Wifi = "none"):
        self.pc_durum = pc_durum
        self.pc_oturum = pc_oturum
        self.pc_pass = pc_pass
        self.programlar = programlar
        self.Wifi = Wifi

    def durum(self):
        if self.pc_durum == "Açık":
            print("Bilgisayar kapatılıyor...")
            time.sleep(2)
            print("_")
            self.pc_durum = "Kapalı"
        else:
            print("Bilgisayar açılıyor...")
            time.sleep(2)
            print("Lütfen Bekleyin...")
            time.sleep(5)
            self.pc_durum = "Açık"

    def oturum(self):
        if self.pc_durum == "Açık":
            self.pc_oturum = input("İsim girin:")
        else:
            pass

    def sifre(self):
        if self.pc_durum == "Açık":
            self.pc_pass = input("Yeni Şifre:")
        else:
            pass

    def program_ekle(self,program_ismi):
        if self.pc_durum == "Açık":
            print("Dosyalar yükleniyor...")
            time.sleep(1)

            self.programlar.append(program_ismi)
        else:
            pass

    def wifi_baglan(self):
        if self.pc_durum == "Açık":
            print("Bağlanılacak bir ağ bulunamadı...\nBir problem olduğunu düşünüyorsan 'Sorun Gidericiyi' çalıştır.")
            x = input("Sorun Gidericiyi çalıştırmak için 'Y' bas")
            if x == "Y":
                print("Sorun bulunuyor...")
                time.sleep(3)
                print("Sorun çözülüyor...")
                time.sleep(3)
                print("Sorun giderilemedi")
                print("HATA: Mavi Ekran :/")
                pc.durum()
        else:
            pass

    def __len__(self):
        if self.pc_durum == "Açık":
            return len(self.programlar)
        else:
            pass

    def __str__(self):
        return "Oturum: {}\nŞifre: {}\nYüklü Uygulamalar: {}\nİnternet : Gerekli donanıma sahip değil".format(self.pc_oturum,self.pc_pass,self.programlar)

pc = bilgisayar()

print("""

Bilgisayar İşlemleri:

1. Bilgisayarı Aç - Kapat
2. Bilgisayarın oturum ismini değiştir (Bilgisayar açık değilse çalışmayacaktır)
3. Bilgisayarın şifresini değiştir (Bilgisayar açık değilse çalışmayacaktır)
4. Bilgisayara Program yükle (Bilgisayar açık değilse çalışmayacaktır)
5. Bilgisayarı Wifi'ya bağla (Bilgisayar açık değilse çalışmayacaktır)
! Bilgisayar bilgilerini yazdır
del Bilgisayarı sıfırla ve programı sonlandır (Bilgisayar açık değilse çalışmayacaktır)
'q' Programı sonlandır

""")

while True:
    islem = input("İşlem girin:")

    if islem == "q":
        print("Program sonlandırıldı...")
        break

    if islem == "1":
        pc.durum()

    if islem == "2":
        pc.oturum()

    if islem == "3":
        pc.sifre()

    if islem == "4":
        if pc.pc_durum == "Açık":
            program_isimleri = input("İndirilecek Uygulama:")

            pc.program_ekle(program_isimleri)
        else:
            pass

    if islem == "5":
        pc.wifi_baglan()


    if islem == "!":
        print(pc)

    if islem == "del":
        if pc.pc_durum == "Açık":
            print("Bilgisayar sıfırlanıyor...")
            time.sleep(3)
            pc.durum()
            del pc
            print("Bilgisayar sıfırlandı...")
            print("Programı tekrar başlat")
            break








