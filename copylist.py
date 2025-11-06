nama = ["Afif", "misel"]
print(f"Nama : \n{nama}")

a = nama
a[0] = "doni"
print(f"hasil : {a}")
print(f"nama : {nama}")


b = nama.copy()
print(f"sblm : {b}")
b[1] = "amira"
print(f"baru : {b}")
