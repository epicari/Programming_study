#
# 백준 1427
# 입력: 2143 출력: 4321
#

n = input()

for i in range(9, -1, -1):
    for j in n:
        if int(j) == i:
            print(i, end='')