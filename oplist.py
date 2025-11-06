angka = [1,2,3,4,2,3,2,1,4,4,2,]
print(f"Data : \n{angka}")

# count data

hitung = angka.count(2)
print(f"Angka 2 ada : {hitung}")

# ambil posisi data index

nama = ["afif", "misel", "amira"]
print(f"Data : \n{nama}")
ambil = nama.index("afif")
print(f"index si afif : {ambil}")

angka.sort()
print(f"sSort : {angka}")

nama.sort()
print(f"Nama asc : {nama}")

# membalik list
nama.reverse()
print(f"data dibalik : {nama}")