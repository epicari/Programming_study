#
# 백준 1924번
#
#

day = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']
day31 = [1, 3, 5, 7, 8, 10, 12]
day30 = [4, 6, 9, 11]
y = 0

a = [0] * 13
for i in range(1, 13):
    if i in day31:
        a[i] = 31
    elif i in day30:
        a[i] = 30
    else:
        a[i] = 28

# 위 작업은 다음과 같이 바꿀 수 있었음
# arrday = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

i, j = map(int, input().split())

for x in range(1, i+1):
    y += a[x]

print(day[(y - (a[i] - j)) % 7])

# for x in range(i-1):
#    y += arrday[x]
# y = (y+j) % 7
# print(day[y])

