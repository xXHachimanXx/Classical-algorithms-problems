
def dfs_rec(start, graph, visited, component):
    visited[start] = True
    component.append(start)
    print(start)

    for next_vertex in range(len(graph)):
        if graph[start][next_vertex] == 1 and \
           not visited[next_vertex]:
           component = dfs_rec(next_vertex, graph, visited, component)

    return component

def dfs(graph, start):
    visited = [False] * len(graph)
    forest = []
    component = []
    for vertex in range(len(graph)):
        if not visited[vertex]:
            component = dfs_rec(vertex, graph, visited, component)
            forest.append(component)
            component = []

    print("Forest: ")
    print(forest)



dfs([
        [0, 1, 0, 1, 0, 0],
        [0, 0, 0, 0, 1, 0],
        [0, 0, 0, 0, 1, 1],
        [0, 1, 0, 0, 0, 0],
        [0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 1],
        
    ], 0)

