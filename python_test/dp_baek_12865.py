#
#
# 다이나믹 프로그래밍
# 백준 12865
#

if __name__ == "__main__":
    n, k = map(int, input().split())
    dp = [[0] * (k + 1) for _ in range(n + 1)]
    print("초기화: ",dp)

    for i in range(1, n + 1):
        weight, value = map(int, input().split())
        for j in range(1, k + 1):
            if j < weight:
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - weight] + value)
                print("j > weight: ", dp)
    
    print(dp[n][k])