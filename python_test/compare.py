print('크기가 두번째로 큰 숫자 찾기')
a = input("비교 할 숫자 입력 A:")
b = input("비교 할 숫자 입력 B: ")
c = input("비교 할 숫자 입력 C: ")

result = a < b if b < c else a < c
if result == True:
    print('B가 두번째로 큼')
else:
    print('A가 두번째로 큼')