#
#
# HackerRank Python Set.add()
#
#

N = int(input())
s = set()

for _ in range(N):
    l = input()
    s.add(l)

print(len(s))

#or

#print(len(set([str(input()) for x in range(int(input()))])))