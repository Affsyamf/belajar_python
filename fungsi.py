def nama():
    print(f"""
Afif Syam Fauzi
6702223011
TK
          """)
nama()


def hallo (nama):
    print(f"Halo {nama}")
    
hallo("Afif")
hallo("misel")
    

# hitung
def hitung (angka1, angka2):
    hasil = angka1 + angka2
    print(f"{angka1} + {angka2} = {hasil}")
    
hitung(1,2)


# list
def anggota (peserta):
    data_peserta = peserta.copy()
    for band in data_peserta:
        print(f"Nama Anggota : {band}")

anggota_band = ["Afif", "opid", "aril"]

anggota(anggota_band)


# menggunakan join
def anggota(band):
    semua = ", ".join(band)
    print(f"Anggota Band : {semua}")
    
anggota_band = ["afif", "misel"]  
anggota(anggota_band)
 
 
#  menggunakan sederhana
def anggota(band):
    print(f"Daftar : {band}")
    
anggota_band = ["chimi", "amira"]
anggota(anggota_band)

# memnaggil satu per satu terpisah
def anggota (band):
    print(f"Anggota 1 : {band[0]}")
    print(f"Anggota 2 : {band[1]}")
    
anggota_band = ["opid", "ayul"]
anggota(anggota_band)

