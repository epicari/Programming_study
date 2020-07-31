#
# 백준 2909 반올림
#

c, k = map(int, input().split())

r = 10**k
d = c // r
s = c % r

if s >= r/2:
    print((d + 1) * r)
else:
    print(d * r)