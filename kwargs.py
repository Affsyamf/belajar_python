# kwargs

'''Kwargs'''
def biodata(nama, nim, umur):
    print(f"Nama : {nama} \nNIM : {nim} \nUmur : {umur}")
biodata("Afif", 3011, 21)    

# kwargs
def biodata(**kwargs):
    nama = kwargs['nama']
    nim = kwargs['nim']
    umur = kwargs['umur']
    print(f"""
Nama : {nama} 
NIM  : {nim}
Umur : {umur}
          """)
    
biodata(nama = "Afif", nim = 2109, umur = 21)


# args dan kwargs
def math(*args, **kwargs):
    output = 0
    if kwargs["option"] == "tambah":
        for angka in args:
            output += angka
    elif kwargs["option"] == "kali":
        output = 1
        for angka in args:
            output *= angka
    else:
        print("Operasi tidak ada")
            
    return output

hasil = math(1,2,3,4, option = "tambah")
print(f"Hasil Tambah : {hasil}")

hasil = math(1,2,3,4, option = "kali")
print(f"Hasil Kali : {hasil}")

 