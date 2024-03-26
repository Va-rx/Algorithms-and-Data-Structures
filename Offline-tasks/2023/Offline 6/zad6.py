from queue import Queue

from zad6testy import runtests
from collections import defaultdict


def znajdz_najwiecej_polaczen(G):
    n = len(G)
    graf = defaultdict(list)

    # Tworzenie grafu dwudzielnego
    for pracownik, umiejetnosci in enumerate(G):
        for maszyna in umiejetnosci:
            graf[pracownik].append(n + maszyna)
            graf[n + maszyna].append(pracownik)

    max_polaczenia = 0
    while True:
        # Inicjalizacja etykiet
        etykiety = [-1] * (n + n)
        etykiety[0] = 0

        # Wyszukiwanie ścieżki powiększającej
        q = Queue()
        q.put(0)
        while not q.empty():
            wierzcholek = q.get()
            if etykiety[wierzcholek] < 0:
                continue
            for sasiad in graf[wierzcholek]:
                if etykiety[sasiad] < 0:
                    etykiety[sasiad] = etykiety[wierzcholek] + 1
                    q.put(sasiad)

        if etykiety[n-1] < 0:
            break

        # Liczenie przepływu
        przeplyw = [0] * (n + n)
        while True:
            f = dfs(graf, przeplyw, etykiety, n, 0, float('inf'))
            if f == 0:
                break
            max_polaczenia += f

    return max_polaczenia


def dfs(graf, przeplyw, etykiety, n, wierzcholek, f):
    if wierzcholek == n-1:
        return f

    for sasiad in graf[wierzcholek]:
        if etykiety[sasiad] == etykiety[wierzcholek] + 1 and przeplyw[sasiad] < f:
            d = dfs(graf, przeplyw, etykiety, n, sasiad, min(f - przeplyw[sasiad], f))
            if d > 0:
                przeplyw[wierzcholek] += d
                przeplyw[sasiad] -= d
                return d

    return 0


def binworker( graph ):
    return znajdz_najwiecej_polaczen(graph)

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( binworker, all_tests = False )
