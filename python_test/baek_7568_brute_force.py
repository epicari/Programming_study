#
# 백준 7568 브루트 포스
#
#

def solution(arr):
    for i in arr:
        rank = 1
        
        for j in arr:
            if i != j:
                if i[0] < j[0] and i[1] < j[1]:
                    rank += 1
        
        print(rank, end = ' ')

if __name__ == '__main__':
    N = int(input())
    arr = []
    for i in range(N):
        x, y = map(int, input().split())
        arr.append((x, y))
    solution(arr)