import sys
from queue import PriorityQueue

maxim = sys.maxsize


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
             4:  {},

        }

n = len(vertices)
dist = [maxim for _ in range(n)]
dist[0] = 0
visited = [False for _ in range(len(vertices))]

pq = PriorityQueue()

pq.put((dist[0], 0))
def dijkstra():
    while not pq.empty():                                                   # 
        current = pq.get()[1]                           
        neighbours = graph[current]
        for vertex, weight in neighbours.items():                           # v*(v - 1)
            if not visited[vertex]:
                dist[vertex] = min(dist[vertex], dist[current] + weight)
                pq.put((dist[vertex], vertex))
        visited[current] = True
dijkstra() 
print(dist)
