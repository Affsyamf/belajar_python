# program list buku
print("\n=== Masukan Buku ===")

list_buku = []
while True:
    judul = input("Masukan Judul Buku :")
    penulis = input("Masukan Nama Penulis :")

    bukub = [judul, penulis]
    list_buku.append(bukub)
    
    print("No. \t| Judul \t\t| Penulis")
    for index,buku in enumerate(list_buku):
        print(f"{index+1}.\t{buku[0]}\t\t\t{buku[1]}")
        
    lanjut = input("Lanjut ? y/n : ")
        
    if lanjut == "n":
            break
        
print("Selesai")
        