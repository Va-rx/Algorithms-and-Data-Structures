def transpose(graph):
    """funkcja transponujaca graf skierowany"""
    glen = len(graph)
    graph_t = [[] for _ in range(glen)]

    for v in range(glen):
        for u in graph[v]:
            graph_t[u].append(v)

    return graph_t

def DFS(G, Przetworzenie):
    n = len(G)
    Visited = [False for _ in range(n)]
    time = 0

    def DFSVISIT(G, v):
        nonlocal time
        time += 1
        Visited[v] = True

        for u in G[v]:
            if not Visited[u]:
                DFSVISIT(G, u)
        time += 1
        Przetworzenie[v] = [time, v]

    for v in range(n):
        if not Visited[v]:
            DFSVISIT(G, v)


def DFSR(G, Przetworzenie):
    n = len(G)
    Visited = [False for _ in range(n)]
    wynik = []

    def DFSVISIT(G, v):
        Visited[v] = True
        for u in G[v]:
            if not Visited[u]:
                DFSVISIT(G, u)
        wynik[-1].append(v)

    for i in range(n):
        v = Przetworzenie[i][1]
        if not Visited[v]:
            wynik.append([])
            DFSVISIT(G, v)

    return wynik


graf = [[3, 2], [0], [1], [4], []]
n = len(graf)

Przetworzenie = [[-1 for _ in range(2)] for _ in range(n)]

DFS(graf, Przetworzenie)
Przetworzenie.sort(key = lambda x: x[0], reverse = True)


# Reversed = graf.copy()
# reverseGraph(Reversed)
# print(Reversed)
# print(DFSR(Reversed, Przetworzenie))

grafNowy = transpose(graf)
print(DFSR(grafNowy, Przetworzenie))

