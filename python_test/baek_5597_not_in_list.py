#
# 백준 5597
#

#N = [x for x in range(1, 31)]
N = list(range(1, 31))
M = [int(input()) for _ in range(28)]

for i in N:
    if i not in M:
        print(i)