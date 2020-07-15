#
# 백준 2810 count
#SLLLLSSLL
#*S*LL*LL*S*S*LL*

n = int(input())
seat = str(input())
ll = seat.count('LL') #3
star = '*'.join(seat).count('*')
res = star - ll + 2

if res > n:
    print(n)
else:
    print(res)