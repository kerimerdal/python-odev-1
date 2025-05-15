# Görev 1: Kullanıcıdan iki sayı alıp işlem yapalım
sayi1 = 10  # Deneme için sayı
sayi2 = 3   # Diğer sayı

print("Toplam:", sayi1 + sayi2)
print("Fark:", sayi1 - sayi2)
print("Çarpım:", sayi1 * sayi2)
print("Bölüm:", sayi1 / sayi2)
print("Mod:", sayi1 % sayi2)
print("Üs alma:", sayi1 ** sayi2)

# Görev 2: 1'den girilen sayıya kadar olanları toplayalım
n = 5  # Örnek sayı
toplam = 0
for i in range(1, n + 1):
    toplam += i
print("Toplam (1'den", n, "e kadar):", toplam)

# Görev 3: 1-100 arasındaki çift sayıları yazdıralım
print("1-100 arası çift sayılar:")
for i in range(1, 101):
    if i % 2 == 0:
        print(i, end=" ")
print()

# Görev 4: Girilen metni tersine çevirelim
metin = "Merhaba"  # Örnek metin
ters_metin = ""
for harf in metin:
    ters_metin = harf + ters_metin
print("Ters hali:", ters_metin)
