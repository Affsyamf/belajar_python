# Date and Time

import datetime as dt

# hari_ini = dt.date.today()
# print(hari_ini)
# print(f"hari ini : {hari_ini:%A}")

# tgl = dt.date(2004,9,21)
# print(tgl)                                             
# print(f"hari ini : {tgl:%A}")

# print("===Tanggal Lahir===")

# tanggal = int(input("Tanggal \t:"))
# bulan = int(input("Bulan \t\t:"))
# tahun = int(input("Tahun \t\t:"))


# print(f""" \n\t===Tanggal lahir===
# Tanggal : {tanggal}
# Bulan   : {bulan}
# Tahun   : {tahun}
            
#       """)

# tl = dt.date(tahun, bulan, tanggal)
# print(f"Tanggal Lahir : {tl} | {tl:%A}")

# Hitung umur

print("\n===Hitung umur===")
hi = dt.date.today()
print(hi)
tanggal = int(input(f"Tanggal : "))
bulan = int(input(f"Bulan : "))
tahun = int(input(f"Tahun : "))
tl = dt.date(tahun, bulan, tanggal)

print(f"Tanggal lahir : {tl}")
print(f"Harinya adalah : {tl:%A}")
print(f"Hari ini tanggal : {hi:%A}")

umur = hi - tl
ut = umur.days // 365
ub  = (umur.days % 365) // 30
print(f"\nUmur kamu sekarang : {ut} Tahun {ub} Bulan")