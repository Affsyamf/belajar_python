import datetime

nama1 = {
    "nama" : "afif",
    "nim" : "3011",
    "sks" : 120,
    "bea" : True,
    "ttl" :datetime.datetime(2004,9,21)
    
}
nama2 = {
    "nama" : "misel",
    "nim" : "3022",
    "sks" : 120,
    "bea" : False,
    "ttl" :datetime.datetime(2005,9,6)
    
}
nama3 = {
    "nama" : "chimi",
    "nim" : "3211",
    "sks" : 120,
    "bea" : False,
    "ttl" :datetime.datetime(2005,4,10)
    
}

data = {
    'MH001' : nama1,
    'MH002' : nama2,
    'MH003' : nama3
}

print(f"{'KEY':<6} {'Nama' : <17} {'Nim':<4} {'SKS':<3} {'Beasiswa':<9} {'Lahir':<10}")

print("-"*50)

for mahasiswa in data:
    KEY = mahasiswa
    
    NAMA= data[KEY]['nama']
    NIM = data[KEY]['nim']
    SKS = data[KEY]['sks']
    BEA = data[KEY]['bea']
    LAH = data[KEY]['ttl'].strftime("%x")

    print(f"{KEY:<6} {NAMA : <17} {NIM:<4} {SKS:<3} {BEA:^9} {LAH:<10}")