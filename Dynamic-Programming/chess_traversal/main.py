from math import inf


def ct(A, i, j):
    n = len(A)

    if i == j == 0:
        return 0

    if i < 0 or j < 0:
        return inf

    return A[i][j] + min(ct(A, i-1, j), ct(A, i, j-1))


def memo_ct(A, i, j):
    n = len(A)
    F = [[-1 for _ in range(n)] for _ in range(n)]
    Path = []

    def inside_memo_ct(i, j):
        if i == j == 0:
            F[i][j] = 0
            return F[i][j]

        if i < 0 or j < 0:
            return inf

        if F[i][j] != -1:
            return F[i][j]

        F[i][j] = A[i][j] + min(inside_memo_ct(i-1, j), inside_memo_ct(i, j-1))
        if inside_memo_ct(i-1, j) < inside_memo_ct(i, j-1):
            Path.append((i, j, i-1, j))
        else:
            Path.append((i, j, i, j-1))

        return F[i][j]

    return Path, inside_memo_ct(i, j)


if __name__ == '__main__':
    n = 4
    A = [[0 for _ in range(n)] for _ in range(n)]
    A[0][0] = 0
    A[0][1] = 1
    A[0][2] = 2
    A[0][3] = 4

    A[1][0] = 3
    A[1][1] = 4
    A[1][2] = 1
    A[1][3] = 30

    A[2][0] = 1
    A[2][1] = 1
    A[2][2] = 1
    A[2][3] = 2

    A[3][0] = 5
    A[3][1] = 8
    A[3][2] = 7
    A[3][3] = 0

    path, result = memo_ct(A, n-1, n-1)
    print(result)
    print(path)
