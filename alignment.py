# width and multiline

# data

nama = "afif"
nim = 670
jurusan = "TK"

data = f"Nama : {nama}, \nnim : {nim}, \nJurusan : {jurusan}"
print(data)

# multiline

data1 =  f"""
Nama    : {nama:>5}
NIM     : {nim:>5}
Jurusan : {jurusan:>5}
"""

print(data1)