

n = 13
g= {
        0: (1,9),
        1: (0, 8),
        2: (3,),
        3: (2, 4, 5, 7),
        4: (3,),
        5: (3, 6),
        6: (5, 7),
        7: (3, 8, 6, 11, 10),
        8: (1, 9, 7),
        9: (0, 8),
        10: (7, 11),
        11: (7, 10),
        12: (),
                }

visited = [false for _ in range(n)]

def dfs(s):
    if visited[s]: return
    visited[s] = True

    neighbours = g[s]
    for neighbour in neighbours:
        dfs(neighbour)

