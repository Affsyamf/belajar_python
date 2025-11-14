# def tambah(a:float, b:float)->float:
#     return a+b

def tambah(*args):
    hasil = 0
    for data in args:
        hasil += data
        
    return hasil

def kali(*args):
    hasil = 1
    for data in args:
        hasil *= data
        
    return hasil

def kurang(*args):
    hasil = args[0]
    for data in args[1:]:
        hasil -= data
        
    return hasil

def pangkat(n:int):
    return lambda angka:angka**n
