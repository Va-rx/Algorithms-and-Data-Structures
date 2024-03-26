# Płowiec Jakub
# Nadzwyczajnie w świecie odpalam program dla 0-wego wierzchołka od bramy polnocnej i pułudniowej. Nastepnie przechodze przez wszystkie
# wierzcholki stosujac zasade podana w tresci polecenia, mozna porownac owy algorytm do problemu skoczka szachowego z backtrackingiem, gdyz
# polega dokladnie na tym samym, gdy nie mamy juz mozliwosci zadnego ruchu w ostatnim miescie, badamy poprzednie
# zlozonosc pamieciowa O(n), czasowa O(n!)
from zad7testy import runtests


#Zwracam wartość 0 gdy wjechalem polnocna, 1 gdy poludniowa
def KtoraBramaWjechalem(G, new_city, city):
    for v in G[new_city][0]:
        if v == city:
            return 0
    return 1


def solve(G, Visited, city, cities, start, wynik, wyjazd_start, wjazd):
    if cities == len(G):
        if wjazd == 0:
            for v in G[city][1]:
                if v == start:
                    return True
        if wjazd == 1:
            for v in G[city][0]:
                if v == start:
                    return True
        return False

    for i in range(2):
        if wjazd == i:
            continue
        for v in G[city][i]:
            new_city = v
            if Visited[new_city] is False:
                wjazd = KtoraBramaWjechalem(G, new_city, city)
                Visited[new_city] = True
                if new_city != start:
                    if solve(G, Visited, new_city, cities+1, start, wynik, wyjazd_start, wjazd):
                        wynik.append(new_city)
                        return True
    Visited[city] = False
    return False


def droga( G ):
    wynik =[]
    cities = 1
    Visited = [False for _ in range(len(G))]
    Visited[0] = True
    wynik.append(0)
    if solve(G, Visited, 0, cities, 0, wynik, 1, 0):
        return wynik
    if solve(G, Visited, 0, cities, 0, wynik, 0, 1):
        return wynik
    return None

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( droga, all_tests = True )