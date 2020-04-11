# 深度优先算法，递归实现


def DFS(graph1, start):
    visit = set()
    degrace(graph1, start, visit)


def degrace(graph1, start, visit):
    visit.add(start)
    print(start)
    for node in graph1[start]:
        if node not in visit:
            degrace(graph1, node, visit)


# 使用dict表示一个无向图
graph = {
    'A': ['B', 'D'],
    'B': ['A', 'D'],
    'D': ['A', 'B', 'C'],
    'C': ['B', 'D', 'E', 'F'],
    'E': ['C'],
    'F': ['C'],
}
DFS(graph, 'A')
