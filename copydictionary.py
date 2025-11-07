# copy dictionary

nama = {
    "a" : "afuf",
    "m" : "misel",
    "c" : "chimi"
}

gg = nama.copy()
print(gg)
print(nama)

gg["c"] = "amira"
print(gg)
print(nama)

# pop dictionary | pop untuk mengambil atau mentransfer dari gg ke luar | berdasarkan key
chimi = gg.pop("c")
print(f"Pop : {gg}")
print(f"data chimi : {chimi}")
print(f"No Pop : {nama}")

# pop items | mengambil dari value terakhir
popi = gg.popitem()
print(f"Popi : {popi}")
print(f"Pop Item : {gg}")
print(f"Asli : {nama}")