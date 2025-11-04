n1 = "afif"
n2 = "syam"
n3 = "fauzi"

nama = n1 + " " + n2 + " " + n3
print(nama)

panjang = len(nama)
print("Panjang dari ", nama, "Adalah : ", panjang)

cari = "s"
status = cari in nama
print("Huruf : ",cari, "Apakah ada pada : ", nama, ",Ya/Tidak : ", status)

print("afif "*2)
print("Index : ", nama[14])
print("Index : 0-3", nama[0:4])
print("Index : 10-15", nama[10:15])
print(nama[14])

print(nama.count("i"))
