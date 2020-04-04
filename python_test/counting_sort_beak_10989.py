#
# 백준 10989
# 계수 정렬(Counting Sort)
# 수의 범위가 정해져 있고 정렬해야 할 때 사용 가능
#
 
import sys

n = int(sys.stdin.readline())
arr = [0] * 10001

for i in range(n):
    data = int(sys.stdin.readline())
    arr[data] += 1

for i in range(10001):
    if arr[i] != 0:
        for j in range(arr[i]):
            print(i)
