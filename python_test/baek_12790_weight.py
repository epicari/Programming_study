#
# 백준 12790
#

""" 런타임에러 남
test_case = int(input())

for _ in range(test_case):
    arr = list(map(int, input().split()))
    
    ca = []
    for i in range(test_case+1):
        ca.append(arr[i]+arr[i+4])

    if ca[0] < 1:
        ca[0] = 1
    if ca[1] < 1:
        ca[1] = 1
    if ca[2] < 0:
        ca[2] = 0

    print((1*ca[0])+(5*ca[1])+(2*ca[2])+(2*ca[3]))
"""

test_case = int(input())
for _ in range(test_case):
    arr = list(map(int, input().split()))

    hp = 1 if arr[0] + arr[4] < 1 else arr[0] + arr[4]
    mp = 1 if arr[1] + arr[5] < 1 else arr[1] + arr[5]
    at = 0 if arr[2] + arr[6] < 0 else arr[2] + arr[6]
    sh = arr[3] + arr[7]

    print((1*hp) + (5*mp) + (2*at) + (2*sh))