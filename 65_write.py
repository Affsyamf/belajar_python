# mode write
# membuat file baru jika tidak ada
# lalu akan menimpa atau overwrite isinya

with open("data_1.txt", 'w', encoding="utf-8") as file:
    file.write("chimika")

with open("data_1.txt", 'w', encoding="utf-8") as file:
    file.write("afif")
    
# 2. mode append
with open("data_2.txt", 'a', encoding="utf-8") as file:
    file.write("afif\n")
with open("data_2.txt", 'a', encoding="utf-8") as file:
    file.write("chimi\n")
with open("data_2.txt", 'a', encoding="utf-8") as file:
    file.write("misel\n")

# 3. moedd r+
with open("data_3.txt", "w", encoding="utf-8") as file:
    file.write("data ke 3\n")

with open("data_3.txt", "r+", encoding="utf-8") as file:
    file.write("Baris-1 \n")
    file.write("Baris-2 \n")
    file.write("Baris-3 \n")
    
with open("data_3.txt", "r+", encoding="utf-8") as file:
    data = file.read()
    print(data)
    
with open("data_3.txt", "r+", encoding="utf-8") as file:
    file.write("baris afif\n")