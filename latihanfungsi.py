# latihan fungsi 
import os


# os.system("cls")

# print(f"{'MENGHITUNG LUAS PERSEGI PANJANG':^40}")
# print(f"{'DAN KELILING PERSEGI PANJANG':^40}\n")
# print(f"{'-'*40}")

# # user input
# LEBAR = int(input("Masukan Lebar :"))
# PANJANG = int(input("Masukan Panjang : "))

# # menghitung luas
# LUAS = PANJANG * LEBAR
# KELILING = 2*(PANJANG+LEBAR)

# # hasil
# print(f"Hasil Luas     : {LUAS}")
# print(f"Hasil Kelilinh : {KELILING}")

# header
def header():
    '''fungsi header'''
    os.system("cls")

    print(f"{'MENGHITUNG LUAS PERSEGI PANJANG':^40}")
    print(f"{'DAN KELILING PERSEGI PANJANG':^40}\n")
    print(f"{'-'*40}")

# user input
def input_user():
    '''Fungsi Input User'''
    panjang = int(input("Masukan Panjang : "))
    lebar = int(input("Masukan Lebar : "))
    
    return panjang, lebar

# Hitung Luas 
def hitung_luas(panjang, lebar):
    return panjang*lebar 

# Hitung Keliling
def hitung_keliling(panjang, lebar):
    return 2*(panjang+lebar)

# Hitung Keduanya
def hitung_dua(panjang, lebar):
    luas = panjang * lebar
    kel = 2*(panjang+lebar)
    return luas, kel

# display
def display(message, value):
    print(f"{message} = {value}")
    
# opsi 
def opsi(panjang,lebar):
    
    print(f"""
1. Untuk Menghitung Luas
2. Untuk Menghitung Keliling
3. Untuk Menghitung Keduanya
          """)
    
    pilih = input("Masukan Pilihan : ")
    if pilih == '1':
        luas = hitung_luas(panjang, lebar)
        display("Hasil Luas : ", luas)
    elif pilih == '2':
       kel = hitung_keliling(panjang, lebar)
       display("Hasil Keliling : ", kel)
    elif pilih == '3':
        luas, keliling = hitung_dua(panjang, lebar)
        display("Hasil Luas : ", luas)
        display("Hasil Keliling : ", keliling)
        
    else:
        print("Tidak Ada Pilihan")
        
        
# program utama
while True:
    header()
    PANJANG, LEBAR = input_user()
    OPSI = opsi(PANJANG, LEBAR)
    LUAS = hitung_luas(PANJANG, LEBAR)
    KELILING = hitung_keliling(PANJANG, LEBAR)
    
    lanjut = input("Lanjut : y/n : ")
    if lanjut == 'n':
        break
    
print("Akhir")
