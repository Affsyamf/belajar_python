data1 = [1,2]
data2 = [3,4]

data3 = [1,2,3,4,5]
data = [data1,data2,data3]
print(f"Data : {data}")

# contoh 
peserta1 = ["afif", 21, "L"]
peserta2 = ["misel", 20, "P"]
peserta3 = ["chimi", 20, "P"]

peserta = [peserta1, peserta2, peserta3]
print(f"Peserta : {peserta}\n")

for nama in peserta:
    print(f"Nama : {nama[0]}")
    print(f"Umur : {nama[1]}")
    print(f"Gender : {nama[2]}\n")
    
pesertac = peserta.copy()
print(f"Pesertac : {pesertac}")
peserta3[0] = "Amira"
print(f"Pesertac : {pesertac}")
print(f"Peserta : {peserta}\n")
    