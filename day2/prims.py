import sys
from queue import PriorityQueue

maxim = sys.maxsize


vertices = [0, 1 ,2, 3, 4, 5, 6]

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
             0:  {1: 2, 2: 3, 3:3},
             1:  {0: 2, 2:4, 4:3},
             2:  {0: 3, 1:4, 3: 5, 4:1, 5:6},
             3:  {0: 3, 2:5, 5: 7},
             4:  {1: 3, 2: 1, 5: 8},
             5:  {3: 7, 2: 6, 4: 8, 6: 9},
             6:  {5: 9}

        }

n = len(vertices)
dist = [maxim for _ in range(n)]
start = 0
dist[start] = 0

pq = PriorityQueue()
for i in range(n):
    pq.put((dist[i], i))

def solve():
    prev = [None for _ in range(n)]
    while not pq.empty():
        current = pq.get()[1]
        neighbours = graph[current]
        for neighbour, weight in neighbours.items():
            if dist[neighbour] > dist[current] + weight:
                dist[neighbour] = dist[current] + weight
                prev[neighbour] = current
                pq.put((dist[neighbour], neighbour))
    
    return prev
  
def prims(s, e):
    path = solve()
    
    return path 

print(prims(0, 6))

