from zad6testy import runtests
from collections import deque

def length(parents, a, b):
    dlugosc = 0
    help = b
    while help is not None:
        if help == a:
            return dlugosc
        help = parents[help]
        dlugosc = dlugosc + 1
    return None


def longer(G, s, t):
    l = len(G)
    visited = [False for _ in range(l)]
    parents = [None for _ in range(l)]
    sciezki = [0 for _ in range(l)]
    Q = deque()

    visited[s] = True
    Q.append(s)
    while Q:
        u = Q.popleft()
        for v in G[u]:
            if not visited[v]:
                visited[v] = True
                parents[v] = u
                Q.append(v)

    for i in range(l):
        sciezki[i] = length(parents, s, i)

    sciezka = sciezki[t]
    # tab = [[] for _ in range(sciezka+1)]
    # tab[sciezka].append(t)


    for i in range(len(tab)-1, 0, -1):
        for j in range(len(tab[i])):
            for v in G[tab[i][j]]:
                if sciezki[v] < sciezki[tab[i][j]] and v not in tab[i-1]:
                    tab[i-1].append(v)
    for i in range(len(tab)-1):
        if len(tab[i]) == 1 and len(tab[i+1]) == 1:
            return tab[i][0], tab[i+1][0]
    return None

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(longer, all_tests=True)
