#
# 백준 10039
#
#

arr = []

for i in range(5):
    score = int(input())
    if score < 40:
        arr.append(40)
    else:
        arr.append(score)

print(round(sum(arr)/5))