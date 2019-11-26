#
# s[::2]는 확장된 split로써, 2배수로 자름
# Hacker를 입력 받으면, Hce akr을 반환
#

if __name__ == '__main__':
    for _ in range(int(input())):
        s = input()
        print(s[::2], s[1::2])