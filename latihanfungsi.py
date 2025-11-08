# latihan fungsi 
import os

os.system("cls")

print(f"{'MENGHITUNG LUAS PERSEGI PANJANG':^40}")
print(f"{'DAN KELILING PERSEGI PANJANG':^40}\n")
print(f"{'-'*40}")

# user input
LEBAR = int(input("Masukan Lebar :"))
PANJANG = int(input("Masukan Panjang : "))

# menghitung luas
LUAS = PANJANG * LEBAR
KELILING = 2*(PANJANG+LEBAR)

# hasil
print(f"Hasil Luas     : {LUAS}")
print(f"Hasil Kelilinh : {KELILING}")

