#
# 백준 1920
# set자료형 ... 중복불가속성 이용
#
n = int(input())
n_num = set(map(int, input().split()))
m = int(input())
m_num = list(map(int, input().split()))

for i in m_num:
    if i not in n_num:
        print('0')
    else:
        print('1')