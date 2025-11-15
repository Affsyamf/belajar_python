# data_input = int(input("Masukan angka : "))

# hasil = 10/data_input
# print(hasil)
from math import nan

# contoh sederhana
# input_user = int(input("Masukan angka : "))
# hasil = nan

# try:
#     hasil = 10/input_user
# except:
#     print("input gaboleh 0")
    
# print(f"Hasil : {hasil}")

# contoh aplimasi

while (True):
    angka = int(input("Masukan angka pembagi : "))
    try:
        hasil = 10/angka
        print(f"Hasil = {hasil}")
        lanjut = input("Lanjut ? y/n : ")
        if lanjut == 'n':
            break
    except:
        print("pembagi 0, masukan input lagi")
print("Akhir 1")

# contoh apk membuat file data.txt
try:
    with open("data.txt", "r") as file:
        print(file.read())
except:
    print(f"file data.txt tidak di temukan, membuat file baru")
    with open("data.txt", "w", encoding="utf-8") as file:
        file.write("file baru")
    
print("akhir program 2")

