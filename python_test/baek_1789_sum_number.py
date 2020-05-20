#
# 백준 1789
# 수의 합 공식 이용하면 됨

i = 0
N = int(input())
while i*(i+1)/2 <= N: i += 1
print(i-1)