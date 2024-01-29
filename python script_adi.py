
try:
    # Kullanıcıdan iki sayı girişi al
    sayi1 = int(input("Birinci sayıyı girin: "))
    sayi2 = int(input("İkinci sayıyı girin: "))

    if sayi1 > sayi2:
        print("Hata: İkinci sayı birinci sayıdan küçük olmalıdır.")
    else:
        print(f"{sayi1} ile {sayi2} arasındaki tek sayılar:")

        # Her bir tek sayıyı ekrana yazdır
        for sayi in range(sayi1, sayi2 + 1):
            if sayi % 2 != 0:  # Modulus işlemi ile sayının tek olup olmadığını kontrol et
                print(sayi)
except ValueError:
    print("Hata: Geçerli bir sayı girişi yapmalısınız.")
