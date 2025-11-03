print("=== PERHITUNGAN SUHU ===")

datafloat = float(input("Masukan Suhu : "))
print ("Suhu : ", datafloat, "Tipe : ", type(datafloat))


# reamour
reamur = (4/5) * datafloat
print("Reamur : ", reamur)

# farenheit
farenheit = (datafloat * 1.8) + 32
print ("Farengeit : ", farenheit)

# kevin
kelvin = datafloat + 273
print ("Kelvin : ", kelvin)