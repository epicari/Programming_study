#
# 백준 2839
# 다른 시각으로 (N -= 3) 바라봐야 코드가 단순해짐...
#

N = int(input())
count = 0

while True:
    if (N % 5) == 0:
        count += (N//5)
        print(count)
        break
    N -= 3
    count += 1
    if N < 0:
        print(-1)
        break