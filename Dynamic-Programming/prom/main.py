from math import inf

def prom(A, i, l1, l2):
    if i >= len(A) or l1 < 0 or l2 < 0:
        if i != 0:
            return -1
        return 0
    else:
        return 1 + max(prom(A, i+1, l1-A[i], l2), prom(A, i+1, l1, l2-A[i]))

def memo_prom(A, i, l1, l2):
    F = [[[None for _ in range(l2+1)] for _ in range(l1+1)] for _ in range(len(A))]

    def prom(i, l1, l2):
        if i >= len(A) or l1 < 0 or l2 < 0:
            if i != 0:
                F[i][l1][l2] = -1
                return F[i][l1][l2]
            F[i][l1][l2] = 0
            return F[i][l1][l2]
        if F[i][l1][l2] is not None:
            return F[i][l1][l2]
        else:
            F[i][l1][l2] = 1 + max(prom(i + 1, l1 - A[i], l2), prom(i + 1, l1, l2 - A[i]))
            return F[i][l1][l2]

    return prom(i, l1, l2)

if __name__ == '__main__':
    A = [5, 4, 3, 3, 3, 2, 4, 8, 8, 3, 5, 4, 1, 4, 6, 2, 4, 5, 6, 5, 3, 2, 5, 1, 1, 2, 3, 6, 7, 8, 9]
    l1 = 47
    l2 = 47
    result = memo_prom(A, 0, l1, l2)
    print(result)
