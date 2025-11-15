#  __main__

print(f"nilai __name__ pada main.py '{__name__}'")

# __name__ pada file program eksternal
import fungsii

# contoh penggunaan

# deklarasi
def tambah(a:int,b:int)->int:
    return a+b


# fungsi utama
if __name__ == "__main__":
    angka1 = 5
    angka2 = 10
    hasil = tambah(angka1,angka2)
    print(f"Hasil : {hasil}")
    
# import package
import package