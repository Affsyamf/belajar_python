# default argumen

def anggota(nama, status = "WNI"):
    print(f"Halo {nama}, Status : {status}")
anggota("Afif", "WNA")
anggota("Misel")


print(f"\n{'='*50}")

# contoh 2
def angka(angka1, angka2 = 5):
    hasil = angka1**angka2
    print(f"Hasil : {hasil}")
    return hasil

angka(angka1 = 5)
print(angka(angka1 = 1))
    
angka(angka1=2)