# Płowiec Jakub
# Algorytm, który właściwie wykonuje wszystkie możliwe ruchy ustawiając wartość maximum na danym polu jako maximum jego sąsiadów +1, gdzie F[0][0] = 0
# Każdy wynik na polu F[n-1][n-1] zapisuje do tablicy wynikowej, z której następnie zwracam maximum jako odpowiedz do zadania
# Tablica F odpowiada za funkcję F(i, j) gdzie oznacza najdluzsza sciezke do pola o indeksach (i, j) od (0, 0).
# Dodatkowo na samym początku sprawdzam, czy ścieżka istnieje.

from zad7testy import runtests
from collections import deque


# Sprawdz czy nie wychodzisz poza tablice, jest sciana, bylo pole juz odwiedzone
def check_valid(F, L, pos_x, pos_y):
    n = len(L)

    if 0 <= pos_x < n and 0 <= pos_y < n and L[pos_y][pos_x] != '#' and F[pos_y][pos_x] == -1:
        return True
    return False


# Wyciagnij najwieksza wartosc z funkcji F od sasiadow
def get_max_neighbour(F, L, pos_x, pos_y):
    n = len(L)

    value1 = -1
    value2 = -1
    value3 = -1

    if 0 <= pos_x-1 < n and 0 <= pos_y < n:
        value1 = F[pos_y][pos_x-1]
    if 0 <= pos_x < n and 0 <= pos_y-1 < n:
        value2 = F[pos_y-1][pos_x]
    if 0 <= pos_x < n and 0 <= pos_y+1 < n:
        value3 = F[pos_y+1][pos_x]

    return max(value1, value2, value3)


# Sprawdzanie sciezki bfs
def is_path(L, move_x, move_y):
    n = len(L)

    Visited = [[-1 for _ in range(n)] for _ in range(n)]
    Visited[0][0] = True
    Q = deque([(0, 0)])

    while Q:
        pos_y, pos_x = Q.popleft()
        if (pos_y, pos_x) == (n-1, n-1):
            return True

        for i in range(3):
            new_pos_y = pos_y + move_y[i]
            new_pos_x = pos_x + move_x[i]
            if check_valid(Visited, L, new_pos_x, new_pos_y):
                Q.append((new_pos_y, new_pos_x))
                Visited[new_pos_y][new_pos_x] = 1

    return False


# Glowna funkcja rekurencyjna
def function(F, L, pos_x, pos_y, move_x, move_y, Visited, Result):
    n = len(L)

    if (pos_x, pos_y) == (n - 1, n - 1):
        Result.append(F[n-1][n-1])
        return

    for i in range(3):
        new_pos_x = pos_x + move_x[i]
        new_pos_y = pos_y + move_y[i]
        if check_valid(F, L, new_pos_x, new_pos_y):
            prev_val = F[new_pos_y][new_pos_x]
            F[new_pos_y][new_pos_x] = get_max_neighbour(F, L, new_pos_x, new_pos_y) + 1
            Visited[new_pos_y][new_pos_x] = True
            function(F, L, new_pos_x, new_pos_y, move_x, move_y, Visited, Result)

            # Backtracking
            Visited[new_pos_y][new_pos_x] = False
            F[new_pos_y][new_pos_x] = prev_val


def maze(L):
    n = len(L)

    move_y = [1, -1, 0]
    move_x = [0, 0, 1]

    if is_path(L, move_x, move_y) is False:
        return -1

    F = [[-1 for _ in range(n)] for _ in range(n)]
    Visited = [[False for _ in range(n)] for _ in range(n)]
    Result = []
    F[0][0] = 0
    Visited[0][0] = True

    function(F, L, 0, 0, move_x, move_y, Visited, Result)
    return max(Result)

# zmień all_tests na True, aby uruchomić wszystkie testy
runtests(maze, all_tests=True)
