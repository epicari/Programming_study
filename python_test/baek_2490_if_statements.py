#
# 백준 2490
#
# 도 1110 A, 개 1100 B, 걸 1000 C, 윷 0000 D, 모 1111 E
for _ in range(3):
    N = list(map(int, input().split()))

    result = N.count(1)

    if result == 4:
        print('E')
    elif result == 3:
        print('A')
    elif result == 2:
        print('B')
    elif result == 1:
        print('C')
    elif result == 0:
        print('D')