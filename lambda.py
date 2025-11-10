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
print(f"Data Angka : {data_angka}")
data_angka.sort()

# sorting tupel angka
data_angka2 = (1,10,4,5,2,3,8,6,9,7)
print(f"Data Angka Tupel : {sorted(data_angka2)}")

