#
# 백준 11399 그리드
#
#

n = int(input())
times = list(map(int, input().split()))
times.sort()
cnt = 0
res = 0
for time in times:
    cnt += time
    res += cnt
print(res)