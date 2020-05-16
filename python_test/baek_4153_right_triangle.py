#
# 백준 4153
# 가장 큰 수를 따로 빼야 함

while True:
    n = list(map(int, input().split()))
    if sum(n) == 0:
        break
    max_n = max(n)
    n.remove(max_n)
    if n[0]**2 + n[1]**2 == max_n**2:
        print('right')
    else:
        print('wrong')