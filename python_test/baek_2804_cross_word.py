#
# 백준 2804 크로스워드
# 백준은 틀렸다고 나오는데 이유를 모르겠음 최적화를 해야할까...
#

a, b = input().split()
arr = [['.' for _ in range(len(a))] for _ in range(len(b))]

status = False
for i in range(len(b)):
    for j in range(len(a)):
        if a[i] == b[j]:
            arr[j] = list(a)
            for k in range(len(b)):
                arr[k][i] = b[k]
            status = True
            break
    if status:
        break

for i in arr:
    print(*i, sep = '') # i가 아닌, *i를 하면 str로 나옴