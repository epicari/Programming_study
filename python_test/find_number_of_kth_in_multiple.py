#
# 
#
#

def solution(a, b, k): # 두 수의 배수를 구한 뒤, 공배수를 찾고 k번째수 반환
    a_set = set()
    b_set = set()

    for i in range(1, 1000001):
        a_set.add(a*i)
        b_set.add(b*i)

        if i == k:
            s = list(a_set | b_set)
            s.sort()
            print(s[k-1])
            break

if __name__ == '__main__':
    a, b, k = map(int, input().split())
    solution(a, b, k)