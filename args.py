# args

def biodata (nama, nim, kelas):
    print(f"""
Nama  : {nama}
NIM   : {nim}
Kelas : {kelas}  
          
        """)
    
biodata("Afif", 3011, "TK01")

def biodata(datalist):
    bio = datalist.copy()
    nama = bio[0]
    nim = bio[1]
    kelas = bio[2]
    
    print(f"""
Nama  : {nama}
NIM   : {nim}
Kelas : {kelas}  
        """)
    
biodata(["Misel", 3022, "TK02"])


# ini args = argumen
def biodata(*args):
    nama = args[0]
    nim = args[1]
    kelas = args[2]
    
    print(f"""
Nama  : {nama}
NIM   : {nim}
Kelas : {kelas}  
        """)
biodata("Chimi", 3045, "TK04")

# kasus penambahan pada args

def jumlah (*data):
    awal = 0
    for angka in data:
        awal += angka
        
    return awal
hasil = jumlah(1,2,3,4,5,6,7,8,9)
print(f"Hasil : {hasil}")
hasil = jumlah(10,5,15)
print(f"Hasil : {hasil}")