# list
# kumpulan data

angka = [1, 2, 3]
print(angka)

nama = ["Afif", "Misel", "Amira"]
print(nama)

data = list(range(0,10))
# list = list(data)
print(data)

# list komprehensi for loop

list_for = [i**2 for i in range(0,10)]
print(list_for)

# list for if

listforif = [i for i in range(0,10) if i != 5]
print(listforif)

# genap
listforif = [i for i in range(0,10) if i % 2 == 0]
print(listforif)

# ganjil
listforif = [i for i in range(0,10) if i % 2 != 0]
print(listforif)