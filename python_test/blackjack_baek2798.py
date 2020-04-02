#
# 백준 2798
# 
#

n, m = map(int, input().split())
num = list(map(int, input().split()))

sum = 0
result = 0

for i in range(n):
    for j in range(i + 1, n):
        for k in range(j + 1, n):
            sum = num[i] + num[j] + num[k]
            if sum <= m:
                result = max(sum, result)

print(result)
