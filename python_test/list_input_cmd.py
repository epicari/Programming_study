#
#
# HackerRank Python List input cmd
#
# eval은 실행 가능한 문자열을 입력받아 문자열을 실행한 결과를 반환함
#

if __name__ == "__main__":
    N = int(input())
    arr = []

    for _ in range(N):
        l = input().split()
        cmd = l[0]
        argv = l[1:]
        if cmd != 'print':
            eval("arr.{0}{1}".format(cmd, tuple(map(int, argv))))
        else:
            print(arr)