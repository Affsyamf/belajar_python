# looping dictionary

nama = {
    "a": "afif",
    "m": "misel",
    "c": "chimi"
}

# looping 1 yang muncul aalah key

for teman in nama:
    print(teman)
    
# looping operator mengambil item

keys = nama.keys()
print(keys)

for keys in nama.keys():
    print(nama.get(keys))
    
for value in nama.values():
    print(value)
    
print(f"\n=============")

for item in nama.items():
    print(item)
    
for key,item in nama.items():
    print(f"Key : {key} Values : {item}")