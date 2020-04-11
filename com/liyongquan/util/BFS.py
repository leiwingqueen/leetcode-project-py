# 广度优先算法


def BFS(graph1, start):
    visit = set()
    queue = []
    visit.add(start)
    queue.append(start)
    while len(queue) > 0:
        node = queue.pop(0)
        print(node + ',')
        for key in graph1[node]:
            if key not in visit:
                visit.add(key)
                queue.append(key)


# 使用dict表示一个无向图
graph = {
    'A': ['B', 'D'],
    'B': ['A', 'D'],
    'D': ['A', 'B', 'C'],
    'C': ['B', 'D', 'E', 'F'],
    'E': ['C'],
    'F': ['C'],
}
BFS(graph, 'A')
