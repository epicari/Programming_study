#
# testcode play by python
#
#

a, b, k = map(int, input().split())
a_set = set()
b_set = set()

for i in range(1, 1000001):
    a_set.add(a*i)
    b_set.add(b*i)

    if i == k:
        s = list(a_set | b_set)
        s.sort()
        print(s[k-1])
        break