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
prev = [None for _ in range(n)]
start = 0
dist[start] = 0

pq = PriorityQueue()
for i in range(n):
    pq.put((dist[i], i))

def kruskals():
    while not pq.empty():
        current = pq.get()
        
