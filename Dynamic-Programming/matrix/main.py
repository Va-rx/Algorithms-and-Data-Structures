from math import inf

def rec_mcp(A, i, j):
    if i == j or i < 0 or j < 0:
        return 0
    return min(rec_mcp(A, ))


def mcp(A):
    n = len(A)
    F = [[0 for _ in range(n)] for _ in range(n)]

    i = 0
    j = 1
    round = 1
    while j != n:
        minn = inf
        for k in range(i, j):
            minn = min(minn, F[i][k] + F[k+1][j] + A[i][0] * A[k][1] * A[j][1])
        F[i][j] = minn

        if j == n-1:
            round += 1

            i = 0
            j = round
        else:
            i += 1
            j += 1
    return F[0][n-1]


if __name__ == '__main__':
    A = [[0 for _ in range(2)] for _ in range(4)]
    A[0][0] = 5
    A[0][1] = 4
    A[1][0] = 4
    A[1][1] = 6
    A[2][0] = 6
    A[2][1] = 2
    A[3][0] = 2
    A[3][1] = 7
    result = mcp(A)
    print(result)
