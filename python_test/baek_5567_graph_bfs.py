#
# 백준 5567 그래프 탐색 BFS
# python의 장점인 dict()와 set() 사용해 빠른 해결법 추가
# 출처: https://underflow101.tistory.com/5
"""
from collections import deque

def bfs(v):
    q = deque([v])
    level = 0
    res = 0
    while q:
        if level == 2:
            break
        level += 1
        v = q.popleft()
        for e in adj[v]:
            if not(visited[e]):
                visited[e] = True
                q.append(e)
                res += 1
    return res
    
n = int(input())
m = int(input())
adj = [[] for _ in range(n+1)]
visited = [False] * (n+1)

for _ in range(m):
    x, y = map(int, input().split())
    adj[x].append(y)
    adj[y].append(x)

print(bfs(1))

"""
n = int(input())
m = int(input())
res = dict()
resSet = set()

for _ in range(m):
    key, item = map(int, input().split())
    if key not in res:
        res[key] = list()
    if item not in res:
        res[item] = list()
    res[key].append(item)
    res[item].append(key)

for key in res[1]:
    resSet.add(key)
    if key not in res:
        continue
    else:
        for item in res[key]:
            resSet.add(item)
#print(resSet) # 1, 2, 3, 4
print(len(resSet) - 1)
