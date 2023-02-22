

n = 13
g = {   0: (9, 7, 11),
        1: (10, 8),
        2: (3, 12),
        3: (2, 4, 7),
        4: (3,),
        5: (6,),
        6: (5,7),
        7: (3, 0, 11, 6),
        8: (1, 12, 9),
        9: (0, 8, 10),
        10: (1, 9),
        11: (0, 7),
        12: (2, 8),
                        }

def solve(s):
    q = []
    q.append(s)

    visited = [False for _ in range(n)]
    visited[s] = True

    prev = [None for _ in range(n)]
    while q:
        node = q.pop(0)
        neighbours = g[node]
        print(node, neighbours)
        for neighbour in neighbours:
            if not visited[neighbour]:
                q.append(neighbour)
                visited[neighbour] = True
                prev[neighbour] = node

    return prev


def reconstruct_path(s, e, prev):
    path = []
    at = e

    while at != None:
        path.append(at)
        at = prev[at]
    
    path.reverse()
    
    if path[0] == s:
        return path
    return []

def bfs(s, e):
    
    prev = solve(s)
    
    return reconstruct_path(s, e, prev)
   
print(bfs(0, 6))
