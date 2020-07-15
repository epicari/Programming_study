#
# 백준 10409 서버
#
#

n, T = map(int, input().split())
num = list(map(int, input().split()))
sum_num = 0
for i, j in enumerate(num):
    if sum_num + j >= T:
        print(i)
        break
    sum_num += j