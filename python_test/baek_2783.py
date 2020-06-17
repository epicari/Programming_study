#
# 백준 2783
#
#

def solution(x, y):
    return (1000 / y) * x

x, y = map(int, input().split())
val1 = solution(x, y)

for _ in range(int(input())):
    x1, y1 = map(int, input().split())
    val2 = solution(x1, y1)
    if val1 > val2:
        val1 = val2

print(round(val1, 2))