import os
rehber={}

def ekle():
    ad=input("Eklenecek İsim: ")
    tel=input("Telefon numarası: ")
    rehber.update({ad:tel})
    print(ad, "eklendi.")

def ara():
    ad=input("Aranacak İsim: ")
    if ad in rehber:
        print(rehber.get(ad))
    else:
        print("Böyle bir isim kayıtlı değil.")

def sil():
    ad=input("Silinecek İsim:")
    if ad in rehber:
        rehber.pop(ad)
        print(f"{ad} silindi.")
    else:
        print("Böyle bir kişi yok.")

def listele():
    print("\n\nİsim           Telefon\n")
    for ad in rehber:
        print(ad, rehber.get(ad))
    print(len(rehber), "kişi listelendi.")
    

while True:
    os.system('cls')

    print("\033[1;32;40m")
    print("╔═══════════════════════════════════╗")
    print("║                                   ║")
    print("║       TELEFON REHBERİ             ║")
    print("║                                   ║")
    print("║   1-Kişi Ekle                     ║")
    print("║   2-Kişi Ara                      ║")
    print("║   3-Kişi Sil                      ║")
    print("║   4-Rehberi Listele               ║")
    print("║                                   ║")   
    print("║    Seçiminiz nedir?               ║")
    print("╚═══════════════════════════════════╝")

    s=input("Seçiminiz nedir?")
    if s=="1":
        ekle()
    elif s=="2":
        ara()
    elif s=="3":
        sil()
    elif s=="4":
        listele()
    input("Devam etmek için enter a basınız.")



    
