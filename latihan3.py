# latihan perulangan membuat segitiga

sisi = 5

# menggunakan for
count = 1
for i in range(sisi):
    print("*" * count)
    count += 1
    
print("\nAkhir For \n")
    
# menggunakan while
count = 1
while True:
    print("*" * count)
    count += 1
    
    if count > sisi:
        break

print("Akhir While")

# hanya ganjil
count = 1
while True:
    if (count % 2):
        # print jika ganjil
        print("*" * count)
        count += 1
    else:
        # akan kembali keatas jika ganjil
        count += 1
        continue
    # berhenti jika count > 5
    if count > sisi:
        break

print("Akhir Ganjil")


# hanya ganjil
count = 1
spasi = int(sisi/2)
print(spasi)
while True:
    if (count % 2):
        # print jika ganjil
        print(" " * spasi, "+" * count)
        spasi -= 1
        count += 1
    else:
        # akan kembali keatas jika ganjil
        count += 1
        continue
    # berhenti jika count > 5
    if count > sisi:
        break
    
while True:
    if (count % 2):
        spasi += 1
        print(" " * spasi, "+" * count)
        count -= 1
    else:
        count -= 1
    if count == 0:
        break
        
print("Akhir Ganjil")