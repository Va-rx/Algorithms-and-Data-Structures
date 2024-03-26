def lcs(A, i, B, j):
    if i < 0 or j < 0:
        return 0
    if A[i] == B[j]:
        return lcs(A, i-1, B, j-1) + 1
    else:
        return max(lcs(A, i-1, B, j), lcs(A, i, B, j-1))


def memo_lcs(A, i, B, j):
    F = [[-1 for _ in range(j+1)] for _ in range(i+1)]

    def memo_inside(i, j):
        if i < 0 or j < 0:
            return 0
        if F[i][j] != -1:
            return F[i][j]
        if A[i] == B[j]:
            F[i][j] = memo_inside(i-1, j-1) + 1
            return F[i][j]
        else:
            F[i][j] = max(memo_inside(i-1, j), memo_inside(i, j-1))
            return F[i][j]

    return memo_inside(i, j)


def tabu_lcs(A, n, B, m):
    F = [[0 for _ in range(n+1)] for _ in range(m+1)]
    for i in range(1, n+1):
        for j in range(1, m+1):
            if A[i-1] == B[j-1]: #  tablice mamy wieksza tj. F[1][1] odpowiada elementom A[0] B[0], stąd uwaga na te minusy dla A oraz B!!!
                F[i][j] = F[i-1][j-1] + 1
            else:
                F[i][j] = max(F[i-1][j], F[i][j-1])
    return F[-1][-1]


if __name__ == '__main__':
    A = 'ABCD'
    B = 'BXAD'
    #result = memo_lcs(A, len(A)-1, B, len(B)-1) # przekazuje indeksy
    result = tabu_lcs(A, len(A), B, len(B)) # przekazuje dlugosc
    print(result)


