# not, or, and, xor

print("===NOT===")
a = False
b = not a
print("Hasil : ", b, type(b))

# jika salah satu ada true maka nilai true
print("===OR===")
a = True
b = False
c = a or b
print("Hasil : ", c, type(c))

# jika salah satu ada false maka nilai false
print("===AND===")
a = True
b = False
c = a and b
print("Hasil : ", c, type(c))

# jika salah satu bernilai true maka true
# jika dua duanya bernilai sama maka false
print("====XOR===")
a = False
b = False
c = a ^ b or False
print("Hasil : ", c, type(c))