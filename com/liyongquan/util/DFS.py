# 深度优先算法(栈的解法)


def DFS(graph1, start):
    visit = set()
    stack = []
    visit.add(start)
    stack.append(start)
    while len(stack) > 0:
        node = stack.pop()
        print(node + ',')
        for key in graph1[node]:
            if key not in visit:
                visit.add(key)
                stack.append(key)

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