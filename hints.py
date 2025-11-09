''' Type Hints untuk fungsi '''

def apa(param):
    hasil = param**2
    print(hasil)
    
apa(2)

def apa(param):
    hasil = param**3
    return hasil

print(apa(4))

# pengunaan type hints
import string

def sepuluh_pangkat(nilai:string) -> string:
    hasil = nilai ** 2
    return hasil

HASIL = sepuluh_pangkat(4)
print(HASIL, type(HASIL))


def fungsi_return(param):
    hasil = param ** 3
    return hasil

y = fungsi_return(4)
dua = y + 1

print(f"Hasil : {y}")
print(f"Hasil : {dua}")


