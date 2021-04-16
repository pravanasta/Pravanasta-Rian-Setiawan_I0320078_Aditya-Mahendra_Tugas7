print(50 * "=")
str = " Program dengan fungsi String "
s = str.center(50,'*')
print(s)
print(50 * "=")

str2= "Silahkan pilih menu"
print("\n", str2.center(50))
print("""
1. Kapital
2. Upper
3. Lower
4. Nomor index
""")

x = int(input("Silahkan pilih: "))
if x == 1:
    print("\nAnda memilih program Kapital")
    teks = input("Masukkan kata: ")
    kapital = teks.capitalize()
    print("Hasil akhir: ", kapital)

elif x == 2:
    print("\nAnda memilih program Upper")
    up = input("Masukkan kata: ")
    upper = up.upper()
    print("Hasil akhir:", upper)

elif x == 3:
    print("\nAnda memilih program Lower")
    low = input("Masukkan kata: ")
    lower = low.lower()
    print("Hasil akhir:", lower)

elif x == 4:
    print("\nAnda memilih pencarian nomor index dalam string")
    kata = input("Masukkan kata/string: ")
    print("Kata anda: ", kata)
    cari = input("Huruf apa yang ingin anda cari: ")
    print( cari, "berada pada index ke: ", kata.find(cari))
else:
    print("Data yang anda masukkan salah")

print("")
print(50 * "=")
str3 = " Selesai "
u = str3.center(50,'*')
print(u)
print(50 * "=")