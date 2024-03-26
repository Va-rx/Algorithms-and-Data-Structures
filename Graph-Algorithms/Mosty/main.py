def DFS(G):
    Visited = [False for _ in range(len(G))]
    Parent = [-1 for _ in range(len(G))]
    Distance = [-1 for _ in range(len(G))]
    Low = [-1 for _ in range(len(G))]
    time = 0
    wynik = []

    def DFSVISIT(G, v):
        nonlocal time
        time += 1
        Visited[v] = True
        Low[v] = Distance[v] = time

        for u in G[v]:
            if not Visited[u]:
                Parent[u] = v
                DFSVISIT(G, u)
                Low[v] = min(Low[u], Low[v]) # dziecko
            if Visited[u] and Parent[v] != u:
                Low[v] = min(Low[v], Distance[u]) # krawedz wsteczna
        time += 1
        if Low[v] == Distance[v] and Parent[v] != -1:
            wynik.append((v, Parent[v]))

    for v in range(len(G)):
        if not Visited[v]:
            DFSVISIT(G, v)
    return wynik


graf = [[1, 2], [0, 3], [0, 4, 5], [1, 5, 4, 6], [2, 3, 6], [2, 3], [4, 7, 3], [6, 8], [7, 9], [8, 7]]
print(DFS(graf))
