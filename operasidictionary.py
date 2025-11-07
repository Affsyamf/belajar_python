data = {
    "a": "afif",
    "m": "misel"
}

# panjang dictionary
LENDICT = len(data)
print(f"Panjang : {LENDICT}")

KEY = "a"
CHECKKEY = KEY in data
print(f"Apakah ada : {KEY} ada di {CHECKKEY}")

# mengakses value read dengan get
print(data["a"])
print(data.get("a"))
print(data.get("k"))

# update ddata
data["a"] = "amira"
print(data)

# menambah
data["b"] = "bool"
print(data)

# hapus
del data["b"]
print(data)

