# fungsi menggunakan return

# fungsi return kuadrat

def kuadrat(input_angka):
    return input_angka**2

y = kuadrat(5)
print(y)
print(kuadrat(10))

z = 10 + kuadrat(7)
print(z)

def tambah (angka1, angka2):
    return angka1 + angka2

a = tambah(3,5)
print(tambah(2,5))
print(a)


# fungsi biasa

def nama():
    print(f"Afif Syam Fauzi")
    
nama()


def nama(user):
    print(f"Nama : {user}")

nama("Misel")


print(f"\n{'='*50}")
# fungsi dengan return banyak
def operasi_mtk(angka1, angka2):
    tambah = angka1 + angka2
    kurang = angka1 - angka2
    kali   = angka1 * angka2
    bagi   = angka1 / angka2
    return tambah, kurang, kali, bagi
    
a,b,c,d = operasi_mtk(2,3)
print(f"Tambah : {a}")
print(f"Kurang : {b}")
print(f"Kali : {c}")
print(f"Bagi : {d}")


