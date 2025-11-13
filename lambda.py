# lambda function

# normal
def kuadrat(angka):
    return angka**2
    
print(f"Hasil : {kuadrat(3)}")

# memakai lambda
k = lambda angka:angka**2
print(f"Lambda : {k(4)}")

tambah = lambda angka1,angka2 : angka1 + angka2
print(f"Hasil tambah : {tambah(3,2)}")

kali = lambda angka1, angka2 : angka1 *angka2
print(f"Hasil Kali : {kali(2,2)}")


# sorting list nama
data_list = ["Afif", "misel", "chimi"]
print(f"Data List : {data_list}")
data_list.sort()

# sorting list angka
data_angka = [1,3,4,2,5]
data_angka.sort()
print(f"Data Angka : {data_angka}")

# sorting tupel angka
data_angka2 = (1,10,4,5,2,3,8,6,9,7)
print(f"Data Angka Tupel : {sorted(data_angka2)}")


data_nama = ["Afif", "Risna", "Louise"]
data_nama.sort()
print(f"Sorted List By Lambda : {data_nama}")

# kasus ganji
angka_baru = [1,2,3,4,5,6,7,8]

def data_angka(angka):
    return angka < 5
data_angka_baru = list(filter(data_angka, angka_baru))
print(f"Hasil angka baru : {data_angka_baru}")

# kasus genap
data_genap = list(filter(lambda x:(x%2==0), angka_baru))
print(data_genap)

# kasus ganjil 
data_ganjil = list(filter(lambda x:(x%2==1), angka_baru))
print(data_ganjil)

# anonymouse function
def pangkat(angka,n):
    return angka**n
print(pangkat(3,2))

def pangkat(n):
    return lambda angka:angka**n

pangkat2 = pangkat(3)
print(f"Hasil Pangkat : {pangkat2(3)}")
print(f"Pangkat : {pangkat(4)(3)}")