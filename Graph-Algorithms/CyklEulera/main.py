def euler(G):
    n = len(G)
    for i in range(n):
        if len(G[i]) % 2 == 1:
            return False
    result = []

    def DFSVISIT(G, u):
        for v in G[u]:
            G[u].remove(v)
            G[v].remove(u)
            DFSVISIT(G, v)
        result.append(u)

    for v in range(n):
        if len(G[v]) > 0:
            DFSVISIT(G, v)
    return result


graf = [[1, 2], [0, 2, 3, 5], [0, 1, 3, 5], [1, 2, 4, 5], [3, 5], [1, 2, 3, 4]]
print(euler(graf))
