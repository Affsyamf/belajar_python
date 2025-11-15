# tutorial membaca file eksternal

print("=== membaca file txt ===")
file = open("data.txt", mode="r")

print(f"Satstus Read : {file.readable()}")
print(f"Satstus Write : {file.writable()}")

# baca seluruh file
print(file.read())

# # baris pertama
# print(file.readline(), end="") 
# # baris kedua
# print(file.readline(), end="") 

# # baca semua baris sebagai list
# print(file.readlines())

print(f"Apakah file sudah di close : {file.closed}")
file.close()
print(f"Apakah file sudah di close : {file.closed}")

# salah satu cara membuika file di py

print("\n=== Membaca txt dengan with ===")
with open("data.txt", mode="r") as file:
    content = file.readline()
    print(content,end="")
    print(f"Apakah file close : {file.closed}")
    
print(f"Apakah file close : {file.closed}")
