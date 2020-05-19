#
# 백준 1748
# 각각의 자릿수를 나누어 계산
# 1의 자릿수는 1부터 N, 10의 자릿수는 10부터 N ... 반복

N = int(input())
ans, i = 0, 1
while i <= N:
    ans += (N-i+1)
    i *= 10
print(ans)