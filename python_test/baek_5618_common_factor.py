#
# 백준 5618 공약수
#
#

arr = [[] for _ in range(3)]
n = int(input())
nums = map(int, input().split())

for i, num in enumerate(nums):
    for j in range(1, num+1):
        if not(num % j):
            arr[i].append(j)
            
if n == 2:
    e = set(arr[0]) & set(arr[1])
else:
    e = set(arr[0]) & set(arr[1]) & set(arr[2])
for i in e: print(i)