# kalkulator sederhana

angka1 = float(input("Masukan angka 1 : "))
operator = input("Pilih : *, +, -, / : ")
angka2 = float(input("Masukan angka 2 : "))


if operator == "+":
    print(f"hasilnya : {angka1 + angka2}")
elif operator == "-":
    print(f"hasilnya : {angka1 - angka2}")
elif operator == "*" or operator == "x":
    print(f"hasilnya : {angka1 * angka2}")
elif operator == "/":
    print(f"hasilnya : {angka1 / angka2}")
else:
    print("Tidak ada operator yang cocok")

print("end")

