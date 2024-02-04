'''
import random

def oyun():
    meyve_listesi = ["elma", "armut", "kiraz", "muz", "üzüm","ananas","vişne","mandalina","portakal","zerdali","muşmula","erik","incil","şeftali","kayısı","papaya","çilek","vanilya","karadut","dut","karpuz","limon","böğütlen","nar","avakado"]
    kullanilan_meyveler = set()

    terminal_meyvesi = ""
    
    while True:
        if terminal_meyvesi == "":
            # Başlangıçta kullanıcının bir meyve girmesini bekleyin
            kullanici_meyvesi = input("İlk meyveyi girin: ").lower()

            if kullanici_meyvesi in meyve_listesi:
                terminal_meyvesi = kullanici_meyvesi
                kullanilan_meyveler.add(terminal_meyvesi)
            else:
                print("Geçerli bir meyve girişi yapmalısınız.")
                break
        else:
            print(f"Terminalin yazdığı meyve: {terminal_meyvesi}")

            kullanici_meyvesi = input("Yeni meyve girin: ").lower()

            # Geçerli bir meyve girişi yapılıp yapılmadığını kontrol et
            if kullanici_meyvesi.isalpha() and kullanici_meyvesi not in kullanilan_meyveler and kullanici_meyvesi[0] == terminal_meyvesi[-1]:
                kullanilan_meyveler.add(kullanici_meyvesi)
                terminal_meyvesi = kullanici_meyvesi
            else:
                print("Yanlış veya daha önce kullanılmış bir meyve girdiniz. Oyun sona erdi.")
                break

if __name__ == "__main__":
    oyun()




import random

def oyun():
    # Oyun başlangıcında rastgele bir meyve seç
    meyve_listesi = ["elma", "armut", "kiraz", "muz", "üzüm","ananas","vişne","mandalina","portakal","zerdali","muşmula","erik","incil","şeftali","kayısı","papaya","çilek","vanilya","karadut","dut","karpuz","limon","böğütlen","nar","avakado"]
    terminal_meyvesi = random.choice(meyve_listesi)

    while True:
        # Kullanıcıdan bir meyve girişi al
        kullanici_meyvesi = input(f"Terminalin yazdığı meyve: {terminal_meyvesi}\nYeni meyve girin: ")

        # Kontrol et ve sonuç bildir
        if kullanici_meyvesi and kullanici_meyvesi[0].lower() == terminal_meyvesi[-1].lower():
            print("Doğru! Sıradaki meyve:")
            terminal_meyvesi = random.choice(meyve_listesi)
        else:
            print("Yanlış! Oyun sona erdi.")
            break

if __name__ == "__main__":
    oyun()
'''


import random

def oyun():
    meyve_listesi = ["elma", "armut", "kiraz", "muz", "üzüm", "ananas", "vişne", "mandalina", "portakal", "zerdali",
                    "muşmula", "erik", "incir", "şeftali", "kayısı", "papaya", "çilek", "vanilya", "karadut", "dut",
                    "karpuz", "limon", "böğürtlen", "nar", "avokado"," trabzon hurması","tomati","tayfan","ahududu","acai","it üzümü","ıspıt","u ile başlıyor"]
    while True:
        # Oyun başlangıcında veya doğru giriş yapıldıktan sonra rastgele bir meyve seç
        terminal_meyvesi = random.choice(meyve_listesi)

        # Kullanıcıdan bir meyve girişi al
        kullanici_meyvesi = input(f"Terminalin yazdığı meyve: {terminal_meyvesi}\nYeni meyve girin: ").lower()

        # Geçerli bir meyve girişi yapılıp yapılmadığını kontrol et
        if kullanici_meyvesi.isalpha() and (kullanici_meyvesi[0].lower() == terminal_meyvesi[-1].lower()) and (kullanici_meyvesi in meyve_listesi):
            print("Doğru! Sıradaki meyve:")
        else:
            print("Yanlış veya geçersiz bir meyve girişi yaptınız. Oyun sona erdi.")
            break

if __name__ == "__main__":
    oyun()
