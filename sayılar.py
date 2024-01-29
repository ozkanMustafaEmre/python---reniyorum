
sayı = input("herangi bir sayı ")

sayıcık = input("herangi bir sayı yaz ")
sayıcıkcık = input("herangi bir sayı yaz ")
print("seni çok seviyorum abla, betül, bla bla, özkan, betül özkan          I LOVE YOU     !")





# Kullanıcıdan sayı girişi al
sayi1 = int(input("Herhangi bir sayı: "))

# Kullanıcıdan bir başka sayı girişi al
sayi2 = int(input("Herhangi bir başka sayı: "))


sayi3 = int(input("Herhangi bir başka sayı: "))

# Toplama işlemi
toplam = sayi1 + sayi2

# Sonucu ekrana yazdır
print("Toplam:", toplam)
sayi1 =  int("herangi bir sayı ")

sayi2 =  int("herangi bir sayı ")
#sayi3 =  input("herangi bir sayı ")
print(sayi1 + sayi2)




# Kullanıcıdan sayı girişi al
sayi1 = int(input("Herhangi bir sayı: "))

# Kullanıcıdan bir başka sayı girişi al
sayi2 = int(input("Herhangi bir başka sayı: "))

# Kullanıcıdan bir başka sayı girişi al
sayi3 = int(input("Herhangi bir başka sayı: "))

sayi4 = int(input("herhangi bir başka sayı: "))


# Toplama işlemi
toplam = sayi1 + sayi2 - sayi3 * sayi4
# Sonucu ekrana yazdır
print("Toplam:", toplam)




def toplama(x, y):
    return x + y

def cikarma(x, y):
    return x - y

def carpma(x, y):
    return x * y

def bolme(x, y):
    if y != 0:
        return x / y
    else:
        return "Bir sayıyı sıfıra bölemezsiniz."

while True:
    try:
        sayi1 = float(input("Birinci sayıyı girin: "))
        sayi2 = float(input("İkinci sayıyı girin: "))
    except ValueError:
        print("Geçerli bir sayı girmelisiniz.")
        continue

    print("Yapmak istediğiniz işlemi seçin:")
    print("1. Toplama")
    print("2. Çıkarma")
    print("3. Çarpma")
    print("4. Bölme")
    print("0. Çıkış")

    secim = input("Seçiminizi yapın (0-4): ")

    if secim == '0':
        print("Programdan çıkılıyor.")
        break
    elif secim == '1':
        print(f"Sonuç: {toplama(sayi1, sayi2)}")
    elif secim == '2':
        print(f"Sonuç: {cikarma(sayi1, sayi2)}")
    elif secim == '3':
        print(f"Sonuç: {carpma(sayi1, sayi2)}")
    elif secim == '4':
        print(f"Sonuç: {bolme(sayi1, sayi2)}")
    else:
        print("Geçersiz bir seçim yaptınız. Lütfen 0 ile 4 arasında bir sayı seçin.")
     



