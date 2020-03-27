#
# Dijkstra Algorithm
# heapq 사용 (우선순위큐)
# 시간 복잡도 = 각 노드마다 인접한 간선들을 모두 검사하는 과정 + 우선순위큐에 삽입/삭제하는 과정
# O(Edge) + O(E log E) = O(E + E log E) + O(ElogE)
#

from heapq import heappush, heappop


def dijkstra(graph, start, end):
    
    #시작 정점에서 각 정점까지의 거리 
    dist = { vertex: [float('inf'), start] for vertex in graph }
    dist[start] = [0, start]
    print("초기 리스트: ",dist)

    heap = []
    heappush(heap, [dist[start][0], start])

    while heap:
        print("heap: ", heap)
        curDist, curVert = heappop(heap)
        print("curDist, curVert: {0}, {1}".format(curDist, curVert))

        if dist[curVert][0] < curDist:
            continue
        
        for adjacent, weight in graph[curVert].items():
            m_dist = curDist + weight
            print("adjacent, curDist, weight: {0} {1} {2}".format(adjacent, curDist, weight))

            if m_dist < dist[adjacent][0]:
                print("m_dist < dist[adjacent][0]: {0} {1}".format(m_dist, dist[adjacent][0]))
                dist[adjacent] = [m_dist, curVert]
                heappush(heap, [m_dist, adjacent])

    path = end
    path_output = end + '->'

    while dist[path][1] != start:
        path_output += dist[path][1] + '->'
        path = dist[path][1]
    
    path_output += start
    print(path_output)

    return dist

if __name__ == "__main__":
    graph = {
        'A': {'B':8, 'C':1, 'D':2},
        'B': {},
        'C': {'B':5, 'D':2},
        'D': {'E':3, 'F':5},
        'E': {'F':1},
        'F': {'A':5}
    }

    print(dijkstra(graph, 'A', 'F'))
