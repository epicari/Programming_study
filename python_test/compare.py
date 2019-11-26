print('두번째로 큰 숫자 찾기')
arr = []
for i in range(3):
    arr.append(input('비교 할 숫자 입력: '))
arr.sort()
if arr[0] == arr[1] or arr[1] == arr[2] or arr[0] == arr[2] == True:
    print('동일한 숫자가 존재함')
else:
    print('결과: {}'.format(arr[1]))