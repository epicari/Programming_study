#
# 백준 2630
# 분할정복 + 쿼드트리
#

def check(x, y, n):
    global white, blue #함수 밖 변수의 값도 수정 가능함
    check_metrix = metrix[x][y]
    
    for i in range(x, x+n):
        for j in range(y, y+n):
            if check_metrix != metrix[i][j]:
                check(x, y, n//2) #1사분면
                check(x, y+n//2, n//2) #2사분면
                check(x+n//2, y, n//2) #3사분면
                check(x+n//2, y+n//2, n//2) #4사분면
                return
    
    if check_metrix:
        blue += 1
        return
    else:
        white += 1
        return

if __name__ == "__main__":
    n = int(input())
    metrix = [list(map(int, input().split())) for _ in range(n)]

    white = 0 #0
    blue = 0 #1

    check(0, 0, n)
    print(white)
    print(blue)