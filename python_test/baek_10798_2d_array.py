#
# 백준 10798
#

arr = []

for _ in range(5):
    arr.append(list(input()))

for i in range(max([len(e) for e in arr])):
    for j in range(5):
        if i < len(arr[j]): #핵심, 없으면 out of range
            print(arr[j][i], end = '')