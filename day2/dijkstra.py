import sys

maxim = sys.maxsize

dist = [0, maxim, maxim, maxim, maxim]

vertices = [0, 1 ,2, 3, 4]

"""
graph = {
             0:  {3: 1, 1: 6},
             1:  {0: 6, 2: 5, 3: 2, 4: 2},
             2:  {1: 5, 4: 5},
             3:  {0: 1, 1: 2, 4: 1},
             4:  {1: 2, 2: 5, 3: 1}

        }
"""
"""
graph = {
             0:  {1: 2, 4: 5},
             1:  {0: 2, 2: 2},
             2:  {1: 2, 3: 2},
             3:  {2: 2, 4: 2},
             4:  {0: 5, 3: 2}

        }
"""
graph = {
             0:  {1: 4, 2: 1},
             1:  {3: 1},
             2:  {1: 2, 3: 5},
             3:  {4: 3},
             4:  {}

        }

visited = [False for _ in range(len(vertices))]

def all_visited():
    for vertex in visited:
        if not vertex:
            return False
    return True

def get_mini(edges):
    mini = maxim
    mini_index = -1
    for node, weight in edges.items():
        if dist[node] < mini:
            mini = dist[node]
            mini_index = node
    return mini_index

def dijkstra():
    current  = 0
    while not all_visited():
        edge = graph[current]    
        for neighbour, weight in edge.items():
            dist[neighbour] = min(dist[neighbour], dist[current] + weight)
        
        visited[current] = True
        current = get_mini(edge)
dijkstra() 
print(dist)
