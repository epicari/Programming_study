#
#
# backtracking
# 백준 9663
# 
#

def dfs(x):
    global result
    if x == n:
        result += 1
    else:
        for i in range(n):
            row[x] = i
            print("탐색 된 row: ", row)

            if check(x):
                dfs(x + 1)

def check(x):
    for i in range(x):
        if row[x] == row[i]:
            return False
        if abs(row[x] - row[i]) == x - i:
            return False 
    return True

if __name__ == "__main__":
    n = int(input())
    row = [0] * n
    print("초기 row: ", row)
    result = 0
    dfs(0)
    print(result)
