#
# 백준 2804 크로스워드
# for 문 3번 썻을 땐 틀렷으나, 수정 후 등록은 맞았음.
#

def solution(a, b):
    arr = [['.' for _ in range(len(a))] for _ in range(len(b))]
    '''
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
    '''
    for i in a:
        if i in b:
            arr[b.index(i)] = list(a)
            for j in range(len(b)):
                arr[j][a.index(i)] = b[j]
            break

    for i in arr:
        print(*i, sep = '') #*iterable 반복가능(iterable)한 자료형 나열

if __name__ == '__main__':
    a, b = input().split()
    solution(a, b)