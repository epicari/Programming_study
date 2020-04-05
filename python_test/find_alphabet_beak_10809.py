#
# 백준 10809
# 
#

s = str(input())
f = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
     'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
i = 0
while True:
    if i == len(f):
        break
    print(s.find(f[i]), end=' ')
    i += 1