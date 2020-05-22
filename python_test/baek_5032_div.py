#
# 백준 5032
# 빈병 9개로 새병3개를 만든 뒤, 다시 새병은 빈병이 되어 새병1개를 만듦

e, f, c = map(int, input().split())

s = e + f
res = 0

while True:
    res += s // c
    s = s // c + s % c

    if s < c:
        break
print(res)