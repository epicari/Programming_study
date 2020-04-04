#
# 백준 1074
# 재귀
# 점화식을 세울 수 있으면 된다
#

def solve(n, x, y):
    global result
    
    if n == 2:
        if x == X and y == Y:
            print(result)
            return
        result += 1
        if x == X and y + 1 == Y:
            print(result)
            return
        result += 1
        if x + 1 == X and y == Y:
            print(result)
            return
        result += 1
        if x + 1 == X and y + 1 == Y:
            print(result)
            return
        result += 1
        return

    solve(n / 2, x, y) # 2^1, 0, 0
    solve(n / 2, x, y + n / 2) # 2^1, 0, 2
    solve(n / 2, x + n / 2, y) # 2^1, 2, 0
    solve(n / 2, x + n / 2, y + n / 2) # 2^1, 2, 2

result = 0
N, X, Y = map(int, input().split(' '))
solve(2 ** N, 0, 0)
