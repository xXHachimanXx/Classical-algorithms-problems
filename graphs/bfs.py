class Vertex:
    def __init__(self, vertex_id, color, dist, dad):
        self.vertex_id = vertex_id
        self.color = color
        self.dist = dist
        self.dad = dad

def bfs_rec(start, graph, queue, visited):
    visited[start] = True
    queue.append(start)

    while queue:
        start = queue.pop(0)
        print(start)
        for i in range(len(graph)):
            if graph[start][i] == 1 and \
               visited[i] == False:
               queue.append(i)
               visited[i] = True


            


def bfs(graph, start):
    # colors = {
    #     "white": 0,
    #     "gray": 1,
    #     "black": 2
    # }
    
    # initialize
    visited = [False] * len(graph)
    queue = []
    bfs_rec(start, graph, queue, visited)

bfs([
        [0, 1, 0, 0, 1, 0, 0, 0],
        [1, 0, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 1, 0, 1, 1, 0],
        [0, 0, 1, 0, 0, 0, 1, 1],
        [1, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 1, 0, 1, 0, 1, 0],
        [0, 0, 1, 1, 0, 1, 0, 1],
        [0, 0, 0, 1, 0, 0, 1, 0],
        
    ], 1)


        
        

