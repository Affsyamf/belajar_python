print("===PERHITUNGAN FARENHEIT KE KELVIN===")

dataf = float(input("Masukan Farenheit : "))
print("Farenheit : ", dataf)

# Konversi ke kelvin
fk = 5/9 * (dataf - 32) + 273
print("Kelvin : ", fk)

# kelvin ke farenheit
datak = float(input("Masukan Kelvin : "))
print("Kelvin : ", datak)

# konnversiu ke farenheit
kf = 9/5  * (datak - 273) + 32
print("Farenheit : ", kf)