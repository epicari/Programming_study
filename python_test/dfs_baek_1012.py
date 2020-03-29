#
#
# 백준 1012 유기농 배추
# dfs 사용
#
#
import sys
sys.setrecursionlimit(100000)

def dfs(x, y):
    visited[x][y] = True
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if nx < 0 or nx >= n or ny < 0 or ny >= m:
            continue
        if arr[nx][ny] and not visited[nx][ny]:
            dfs(nx, ny)

if __name__ == "__main__":
    for _ in range(int(input())):
        m, n, k = map(int, input().split())
        arr = [[0] * m for _ in range(n)]
        visited = [[False] * m for _ in range(n)]

        for _ in range(k):
            y, m = map(int, input().split())
            arr[x][y] = 1
        
        result = 0

        for i in range(n):
            for j in range(m):
                if arr[i][j] and not visited[i][j]:
                    dfs(i, j)
                    result += 1

        print(result)
