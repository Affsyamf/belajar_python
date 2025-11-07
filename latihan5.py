# dict mahasiswa
import datetime
import os
mahasiswa = {
    "nama" : "nama",
    "nim" : "0000",
    "sks" : 0,
    "ttl" : datetime.datetime(1111,1,11)
}

data_mhs = {}

os.system("cls")
print(f"{'Selamart Datang':^20}")
print(f"{'Data Mahasiswa':^20}")
print("-"*20)

mahasiswa = dict.fromkeys(mahasiswa.keys())
mahasiswa['nama'] = input("Masukan Nama : ")
mahasiswa['nim'] = input("Masukan Nim : ")
mahasiswa['sks'] = input("Masukan SKS : ")
TAHUN_LAH = int(input("Tahun lahir (YYYY) : "))
BULAN_LAH = int(input("Bulan Lahir (MM) : "))
TGL_LAH  = int(input("Tanggal Lahir (DD) : "))
mahasiswa ['ttl'] = datetime.datetime(TAHUN_LAH, BULAN_LAH, TGL_LAH)
print(mahasiswa)


