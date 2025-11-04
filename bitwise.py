a = 9
b = 5

# bitwise OR
c = a | b
print("nilai : ", a, "Binary : ", format(a, "08b")) 
print("nilai : ", b, "Binary : ", format(b, "08b")) 
print("-----------------------------")
print("nilai : ", c, "Binary : ", format(c, "08b")) 


print("====AND====")
c = a & b
print("nilai : ", a, "Binary : ", format(a, "08b")) 
print("nilai : ", b, "Binary : ", format(b, "08b"))
print("-----------------------------") 
print("nilai : ", c, "Binary : ", format(c, "08b")) 

# bitwise XOR
print("====XOR====")
c = a ^ b
print("nilai : ", a, "Binary : ", format(a, "08b")) 
print("nilai : ", b, "Binary : ", format(b, "08b"))
print("-----------------------------") 
print("nilai : ", c, "Binary :", format(c, "08b"))

# bitwise NOT
print("====NOT====")
c = ~a
print("nilai : ", b, "Binary : ", format(b, "08b")) 
print("-----------------------------") 
print("nilai : ", c, "Binary :", format(c &0xFF, "08b"))

# bitwise geser
print("====Geser====")
c = a << 2
print("nilai : ", a, "Binary : ", format(a, "08b")) 
print("-----------------------------") 
print("nilai : ", c, "Binary :", format(c, "08b"))