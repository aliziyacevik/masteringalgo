import sys

maxim = sys.maxsize

adj_list = {
        'S': {'E' : 8, 'A': 10},
        'A': {'C': 2,},
        'B': {'A': 1,},
        'C': {'B': -2,},
        'D': {'A': -4,},
        'E': {'D': 1,}
    
        }

dist = {node: maxim for node in adj_list.keys() }
prev = {node: None for node in adj_list.keys() }


def bellman_ford(start):
    dist[start] = 0
    for i in range(5):
        for current, edges in adj_list.items():
            for nextt, weight in edges.items():
                dist[nextt] = min(dist[nextt], dist[current] + weight)
print(dist)
bellman_ford('S')
print(dist)
