#
# 백준 4948 소수 찾기
# 에라토스테네스의 체 사용하면 빠름

N = (123456*2)+1

#에라토스테네스의 체
sieve = [True] * N
for i in range(2, int(N**0.5)+1):
    if sieve[i]:
        for j in range(2*i, N, i):
            sieve[j] = False

while True:
    val = int(input())
    if val == 0:
        break
    cnt = 0

    for i in range(val+1, (val*2)+1):
        if sieve[i]:
            cnt += 1

    print(cnt)