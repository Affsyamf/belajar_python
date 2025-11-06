data1 = [1,2]
data2 = [3,4]

data2d = [data1, data2, 10]
data2dc = data2d.copy()
print(f"Data \t:{data2d}")
print(f"Data Copy :{data2dc}")

# ambil data dari nestedlist
# data = data2d[0][0]
# print(f"Data : {data}")

data2d [1][0] = 5
data2d [2] = 9
print(f"ata : {data2d}")
print(f"data : {data2dc}")

from copy import deepcopy

data2d = [data1, data2, 10]
datadeep = deepcopy(data2d)

data2d[1][0] = 30
print(f"Data awal : {data2d}")
print(f"Data copy : {data2dc}")
print(f"Data deep : {datadeep}")

