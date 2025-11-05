# continue and pass

angka = 0
# kata = ["Afif", "Chimi"]

# while angka < 5:
#     angka += 1
#     if angka == 3:
#         print("GG")
        
#     print(angka)
    
# for nama in kata:
#     print(nama)

# continue

print(f"Angka skrg : {angka}")

while angka < 5:
    angka += 1
    print(f"Angka : {angka}") 
    
    if angka == 3:
        print("GG")
        continue
    
    print(f"Afif")
    
print("end")