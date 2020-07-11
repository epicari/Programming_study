#
# 백준 1188 최대공약수 & 서로소
# 
# https://www.acmicpc.net/problem/1188
# 소시지 a개를 b명에게 준다 is (소시지 a/g 개를 b/g명에게) * g
# g는 a와 b의 최대공약수이며, 위에서 a b를 g로 먼저 나눴으므로 서로소가 됨
# 따라서, b - GCD(a, b)

def solution(n, m):
    if n % m == 0:
        return m
    return solution(m, n%m)

if __name__ == '__main__':
    n, m = map(int, input().split())
    print(m - solution(n, m))