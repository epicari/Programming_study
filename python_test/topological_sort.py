#
# 백준 1766
# 위상정렬(Topological Sort)
# 순서가 정해진 작업
#

import heapq

if __name__ == "__main__":
    n, m = map(int, input().split()) #문제의 수와 먼저 풀어야 할 문제에 대한 정보의 개수
    array = [[] for _ in range(n + 1)]
    indegree = [0] * (n + 1) #진입차수 확인

    heap = []
    result = []

    for _ in range(m): #먼저 풀어야 할 문제에 대한 정보의 개수 만큼 반복
        x, y = map(int, input().split())
        array[x].append(y) #x가 먼저 풀어야 할 문제
        indegree[y] += 1
        print("array: ",array)
        print("indegree: ", indegree)

    for i in range(1, n + 1):
        if indegree[i] == 0:
            heapq.heappush(heap, i)
            print("heap: ", heap)

    while heap:
        data = heapq.heappop(heap)
        print("data: ", data)
        result.append(data)
        for y in array[data]:
            indegree[y] -= 1
            print("after indegree: ", indegree)
            if indegree[y] == 0:
                heapq.heappush(heap, y)
                print("after heap: ", heap)
    
    for i in result:
        print(i, end=' ')