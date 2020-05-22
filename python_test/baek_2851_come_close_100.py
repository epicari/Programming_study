#
# 백준 2851
#

arr = []
res = 0

for _ in range(10):
    arr.append(int(input()))

for i in arr:
    res += i
    if res >= 100:
        if res == 100:
            break
        else:
            if res - 100 > 100 - (res - i):
                res -= i
            break

print(res)