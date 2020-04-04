#
# 백준 10814
#
#

n = int(input())
name_age = []

for _ in range(n):
    data = input().split(' ')
    name_age.append((int(data[0]), data[1]))

name_age = sorted(name_age, key=lambda x: x[0])

for i in name_age:
    print(i[0], i[1])

