import datetime

data_waktu = datetime.datetime.now()
print(f"waktu sekarang : {data_waktu}")
print(f"Tahun : {data_waktu.year}")
print(f"Tahun : {data_waktu.strftime('%A')}")

from collections import Counter

data = ["a", "b", "c", "a", "b"]
data_count = Counter(data)

print(f"Data count : {data_count}")
print(f"Data A : {data_count['a']} ")
print(f"Data B : {data_count['c']} ")

import io

file = io.open("file_text.txt", "r")
print(file.read())


# count = 0
# for i in data:
#     if i == 'a':
#         count += 1
    
# print(count)