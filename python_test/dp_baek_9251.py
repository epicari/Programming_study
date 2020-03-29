#
#
# 다이나믹 프로그래밍
# 백준 9251
#

if __name__ == "__main__":
    x = input()
    y = input()

    dp = [[0] * (len(y) + 1) for _ in range(len(x) + 1)]
    print("초기 dp: ", dp)

    for i in range(1, len(x) + 1):
        for j in range(1, len(y) + 1):
            if x[i - 1] == y[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
                print("일치하는 값이 있을 때: ", dp)
            else:
                dp[i][j] = max(dp[i][j - 1], dp[i - 1][j])
                print("일치하는 값이 없을 때: ", dp)

    print(dp[len(x)][len(y)])