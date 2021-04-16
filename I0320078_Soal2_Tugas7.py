print(50 * "=")
str = " Program dengan fungsi Numerik "
s = str.center(50,'*')
print(s)
print(50 * "=")

import math

str2= "Silahkan pilih menu"
print("\n", str2.center(50))
print("""
1. Nilai mutlak
2. Nilai akar
3. Pembulatan kebawah
4. Pembulatan ke atas
""")

x = int(input("Silahkan pilih: "))
if x == 1:
    print("\nAnda memilih program nilai mutlak")
    angka = int(input("Masukkan angka: "))
    print("|",angka,"|= ", abs(angka) )

elif x == 2:
    print("\nAnda memilih program pencarian akar")
    angka2 = int(input("Masukkan angka: "))
    print("Akar dari", angka2, "adalah ", math.sqrt(angka2))

elif x == 3:
    print("\nAnda memilih program pembulatan ke bawah")
    angka3 = float(input("Masukkan angka: "))
    print("Pembulatan ke bawah dari", angka3, "adalah ", math.floor(angka3))

elif x == 4:
    print("\nAnda memilih program pembulatan ke atas")
    angka4 = float(input("Masukkan angka: "))
    print("Pembulatan ke atas dari", angka4, "adalah ", math.ceil(angka4))

else:
    print("Data yang anda masukkan salah")

print("")
print(50 * "=")
str3 = " Selesai "
u = str3.center(50,'*')
print(u)
print(50 * "=")