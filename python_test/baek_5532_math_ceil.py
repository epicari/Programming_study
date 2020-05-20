#
# 백준 5532
# math.ceil()을 쓰면 소숫점을 모두 올림 시킴
# round()는 반올림

from math import ceil

L = int(input())
A = int(input())
B = int(input())
C = int(input())
D = int(input())

print(L - max(ceil(A/C), ceil(B/D)))