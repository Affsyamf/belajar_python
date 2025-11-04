# operator dalam method

salam = "Halo"
print(f"Afif {salam}")
print(f"afif {salam}".capitalize())
print(salam.capitalize())
print(salam.upper())
print(salam.lower())
print("Apakah kecil : " + str(salam.islower()))
print("Apakah Upper : " + str(salam.isupper()))

nama = "Afif Syam Fauzi"
print("Cek : " + str(nama.isalpha()))
print("Cek : " + str(nama.isascii()))
print("Cek : " + str(nama.isdecimal()))
print("Cek : " + str(nama.isalnum()))
print("Cek : " + str(nama.isdigit()))
print("Cek : " + str(nama.isspace()))

name = nama.replace("Afif", "Eka")
print(name)



nama = ["Afif","Syam","Fauzi"]
print(nama)
print(", ".join(nama))
print(" ".join(nama))

nama = "afif1syam1fauzi"
print(nama)
print(nama.split("1"))