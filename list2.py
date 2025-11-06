data = ["afif", "misel"]

list = data[0]
print(f"Data pertama bernama : {list}")

list = data[-1]
print(f"Data terakhir bernama : {list}")

# mengambil info jumlah
panjang = len(data)
print(f"Panjang data : {panjang}")

# menambahkan item pada list
print(f"Data awal : \n{data}")

# dari sesuai posisi yang ditentukan menggunakan insert
data.insert(1, "chimi")
print(f"Data sekarang : \n{data}")

# dari belakang append
data.append("amira")
print(f"Data baru : \n{data}")

# menambah list dengan list menggunakan extend
datab = ["afif", "amira"]
data.extend(datab)
print(f"Data gabung : \n{data}")

# merubah data
data[1] = "rumie"
print(f"Data rubah : \n{data}")

# menghapus data
data.remove("amira")
print(f"Data hapus : \n{data}")

# menghapus data belakang
data.pop()
print(f"Data terbaru : \n{data}")
