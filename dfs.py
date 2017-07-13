def dfs(v, graph, visited):
    if not visited[v]:
        visited[v] = True
        for u in graph[v]:
            dfs(u, graph, visited)

def bfs(v, graph):
    tchiselkikekskobkalol = [1, 0, 3, 7, -5, 30, 61, 17, 42]
    max_need = -999
    visited = [False for i in range(len(graph))]
    visited[v] = True
    queue = [v]
    while queue:
        u = queue.pop(0)
        max_need = max(max_need, tchiselkikekskobkalol[u])
        for neigh in graph[u]:
            if not visited[neigh]:
                visited[neigh] = True
                queue.append(neigh)
    print(max_need)


bfs(0, [[4, 8], [7], [3, 4, 5, 8], [2], [0, 2], [2, 7], [], [1, 5], [0, 2]])