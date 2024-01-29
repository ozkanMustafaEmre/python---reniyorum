'''
# Kullanıcıdan sayı girişi al
sayi1 = int(input("Herhangi bir sayı: "))

# Kullanıcıdan bir başka sayı girişi al
sayi2 = int(input("Herhangi bir başka sayı: "))

# Kullanıcıdan bir başka sayı girişi al
bişey = (input("herangi başka bir işlem: "))

# Sonucu ekrana yazdır
if bişey == "+ ":
 print(sayi1 + sayi2)
ccc
# Kullanıcıdan sayı girişi al
sayi1 = int(input("Herhangi bir sayı: "))

# Kullanıcıdan bir başka sayı girişi al
sayi2 = int(input("Herhangi bir başka sayı: "))

# Kullanıcıdan bir işlem seçimi al
bişey = input("Toplama işlemi için '+' yazın: ")

# Kullanıcıdan sayı girişi al
sayi1 = int(input("Herhangi bir sayı: "))

# Kullanıcıdan bir başka sayı girişi al
sayi2 = int(input("Herhangi bir başka sayı: "))

# Kullanıcıdan bir işlem seçimi al
bişey = input("Toplama işlemi için '+' yazın: ")

# Kullanıcının girdiği işlemi kontrol et ve sonucu ekrana yazdır
if bişey == '+':
    sonuc = sayi1 + sayi2
    print(f"Sonuç: {sonuc}")
else:
    print("Geçersiz bir işlem seçtiniz. Lütfen sadece '+' işlemi için geçerli bir değer girin.")


 Kullanıcının girdiği işlemi kontrol et ve sonucu ekrana yazdır
if bişey == '-':
    sonuc = sayi1 - sayi2
    print(f"Sonuç: {sonuc}")
else:
    print("Geçersiz bir işlem seçtiniz. Lütfen sadece '-' işlemi için geçerli bir değer girin.")
'''


# Kullanıcıdan sayı girişi al
sayi1 = int(input("Herhangi bir sayı: "))

# Kullanıcıdan bir başka sayı girişi al
sayi2 = int(input("Herhangi bir başka sayı: "))

# Kullanıcıdan bir işlem seçimi al
bişey = input("Geçersiz bir işlem seçtiniz. Lütfen sadece '+' ,'-','/','*' işlemi için geçerli bir değer girin.Toplama işlemi için '+' veya çıkarma işlemi için '-' yazın: ")

# Kullanıcının girdiği işlemi kontrol et ve sonucu ekrana yazdır
if bişey == '+':
    sonuc = sayi1 + sayi2
    print(f"Sonuç: {sonuc}")
elif bişey == '-':
    sonuc = sayi1 - sayi2
    print(f"Sonuç: {sonuc}")
elif bişey == '/':
    sonuc = sayi1 / sayi2
    print(f"Sonuç: {sonuc}")
elif bişey == '*':
    sonuc = sayi1 * sayi2
    print(f"Sonuç: {sonuc}")

else:
    print("Geçersiz bir işlem seçtiniz. Lütfen sadece '+' ,'-','/','*' işlemi için geçerli bir değer girin.")
