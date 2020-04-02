#
# 백준 2920
# 
#

n = list(map(int, input().split(' ')))

ascending = True
descending = True

for i in range(1, 8):
    if n[i] < n[i - 1]:
        ascending = False
    elif n[i] > n[i - 1]:
        descending = False 

if ascending:
    print("ascending")
elif descending:
    print("descending")
else:
    print("mixed")