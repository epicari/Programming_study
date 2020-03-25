#
# bfs, dfs
# 시간 복잡도 = O(노드수+간선수)
#
#

def bfs(graph, root):
    visiting = []
    visited = []

    visiting.append(root)

    while visiting:
        print("visit: ", visiting)
        node = visiting.pop(0)
        print("visiting node: ", node)
        if node not in visited:
            visited.append(node)
            print("add node to visited", visited)
            visiting.extend(graph[node])
    
    return visited    

def dfs(graph, root):
    visited = []
    visiting = []

    visiting.append(root)

    while visiting:
        print("visit: ", visiting)
        node = visiting.pop()
        print("visiting node: ", node)
        if node not in visited:
            visited.append(node)
            print("add node to visited", visited)
            visiting.extend(graph[node])

    return visited

if __name__ == "__main__":
    graph = dict()
    graph['A'] = ['B', 'C']
    graph['B'] = ['A', 'D']
    graph['C'] = ['A', 'G', 'H', 'I']
    graph['D'] = ['B', 'E', 'F']
    graph['E'] = ['D']
    graph['F'] = ['D']
    graph['G'] = ['C']
    graph['H'] = ['C']
    graph['I'] = ['C', 'J']
    graph['J'] = ['I']

    print(graph)

    dfs(graph, 'A')