# looping list
# for loop

angka = [1,2,3,4,5]
print(f"Angka - {angka}")

for i in angka:
    print(f"angka : {i}")
    

# list comprehension
data = ["afif", "misel", "amira"]
[print(f"nama : {i}") for i in data]


# enumerate
data = ["afif", "misel", "amira"]

for index,urut in enumerate(data):
    print(f"index - {index}, data - {urut}")