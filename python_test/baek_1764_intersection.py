#
# 백준 1764
# set1 & set2 == set1.intersection(set2)

N, M = map(int, input().split())
str1, str2 = set(), set()

for _ in range(N):
    str1.add(input())

for _ in range(M):
    str2.add(input())

res = list(str1 & str2) #intersection

print(len(res))

for j in sorted(res):
    print(j)