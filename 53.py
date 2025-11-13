# global dan local scope


nama = "Misel"
def panggil_nama():
    nama = "Afif"
    print(f"Nama : {nama}")
panggil_nama()

# variabel global dalam loop

for i in range(0,3):
    print(f"Nama : {i} {nama}")
    
    
angka = 2
nama = "afif"

def ubah(n, y):
    global angka
    global nama
    nama = y
    angka = n
print(f"hasil : {angka, nama}")
ubah(10, "misel")
print(f"Hasil bawah : {angka, nama}")


# contoh 3
angka = 0

for i in range (0,5):
    angka += i
    angka_dummy = 0
print(angka)
print(angka_dummy)

if True:
    angka = 10
    angka_dummy = 10
    
print(angka)
print(angka_dummy)
