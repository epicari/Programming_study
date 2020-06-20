#
# 백준 11047 그리드
#
#

n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]
coins.sort(reverse=True)
cnt = 0
for coin in coins:
    if coin < k:
        cnt += k // coin
        k %= coin
        if k == 0:
            break
print(cnt)