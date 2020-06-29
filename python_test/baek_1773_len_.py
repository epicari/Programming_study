#
# 백준 1773 폭죽쇼 (= 공배수는 한 번만 샘)
# 두가지 방법이 있으나, 둘 다 시간초과 나옴..
#

n, c = map(int, input().split())
sets = set()
for _ in range(n):
    m = int(input())
    for j in range(m, c+1, m):
        sets.add(j)
print(len(list(sets)))

check = [False] * (c+1)
ans = 0
for _ in range(n):
    x = int(input())
    for y in range(x, c+1, x):
        if not check[y]:
            check[y] = True
            ans += 1
print(ans)