#
# Hacker Rank 30 Days of Code Day 26: Nested Logic
#
# 

a = list(map(int, input().split())) # 2 6 2015
e = list(map(int, input().split())) # 5 7 2015

i, j, k = 0, 1, 2

if a == e:
    print('0')
else:   
    if a[k] != e[k]:
        if (a[k] - e[k]) < 0: print('0')
        else: print('10000')
    else:
        if a[j] != e[j]:
            if (a[j] - e[j]) < 0: print('0')
            else:
                print(500 * (a[j] - e[j]))
        else:
            if (a[i] - e[i]) < 0: print('0')
            else:
                print(15 * (a[i] - e[i]))

#
d, m, y = map(int, input().split(' '))
D, M, Y = map(int, input().split(' '))
print(0 if (y,m,d) <= (Y,M,D) else 10000 if y > Y else (m-M)*500 if m > M else (d-D)*15)