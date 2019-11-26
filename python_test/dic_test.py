#
# 딕셔너리의 key와 value를 입력받고, 찾고자 하는 key를 입력받아 그에 해당하는 value 반환
# 입력 받은 key에 해당된 value가 없으면 Not found 반환
# 입력이 없을 경우 break를 걸기 위해 try except 사용
#

if __name__ == '__main__':
    N = int(input())
    mydict = dict()
    for _ in range(N):
        x = input().split()
        mydict[x[0]] = x[1]
    while True:
        try:
            k = input()
            if k in mydict:
                print(k, '=', mydict[k], sep="")
            else:
                print('Not found')
        except EOFError as error:
            break