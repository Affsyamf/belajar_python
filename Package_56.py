import sains.matematika
from sains import fisika
from sains.fisika import gaya as gayas

hasil_tambah = sains.matematika.tambah(1,2,3,4,5)
print(f"Hasil tambah dari package adalah = {hasil_tambah}")

gaya = fisika.gaya(90,10)
print(f"Hasil gaya : {gaya}")
gaya = gayas(90,10)
print(f"Hasil gaya : {gaya}")