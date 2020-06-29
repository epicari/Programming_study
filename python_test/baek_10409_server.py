#
# 백준 10409
#
#

n, T = map(int, input().split())
num = list(map(int, input().split()))
sum_num = 0
cnt = 0
for i in num:
    if sum_num + i > T:
        print(cnt)
        break
    sum_num += i
    cnt += 1