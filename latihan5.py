# dict mahasiswa
import datetime
import os
import string
import random

mahasiswa_tem = {
    "nama" : "nama",
    "nim" : "0000",
    "sks" : 0,
    "ttl" : datetime.datetime(1111,1,11)
}

data_mhs = {}

while True:
    os.system("cls")
    print(f"{'Selamart Datang':^20}")
    print(f"{'Data Mahasiswa':^20}")
    print("-"*20)

    mahasiswa = dict.fromkeys(mahasiswa_tem.keys())
    mahasiswa['nama'] = input("Masukan Nama : ")
    mahasiswa['nim'] = input("Masukan Nim : ")
    mahasiswa['sks'] = int(input("Masukan SKS : "))
    TAHUN_LAH = int(input("Tahun lahir (YYYY) : "))
    BULAN_LAH = int(input("Bulan Lahir (MM) : "))
    TGL_LAH  = int(input("Tanggal Lahir (DD) : "))
    mahasiswa ['ttl'] = datetime.datetime(TAHUN_LAH, BULAN_LAH, TGL_LAH)
    
    KEY = ''.join((random.choice(string.ascii_uppercase) for i in range(6)))
    data_mhs.update({KEY:mahasiswa})

	# dari tutorial sebelumnya, hilangkan beasiswa
    print(f"\n{'KEY':<6} {'Nama':<17} {'NIM':<8} {'SKS':<10} {'Tanggal Lahir':<10}")
    print('-'*60)

    for mahasiswa in data_mhs:
        KEY = mahasiswa
        
        NAMA = data_mhs[KEY]['nama']
        NIM  = data_mhs[KEY]['nim']
        SKS  = data_mhs[KEY]['sks']
        TTL  = data_mhs[KEY]['ttl'].strftime("%x")
        
        print(f"{KEY:<6} {NAMA:<17} {NIM:<8} {SKS:^10} {TTL:^10}")
        
    print('\n')
    lanjut = input("lanjut y/n : ")
    if lanjut.lower() == 'n':
        break

print("Akhir")

