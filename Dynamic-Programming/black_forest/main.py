def blackforest(A, i):
    if i == 0:
        return A[0]
    if i == 1:
        return max(A[0], A[1])
    return max(blackforest(A, i-1), blackforest(A, i-2) + A[i])


def mem_blackforest(A, i):
    n = len(A)
    F = [-1 for _ in range(n)]

    def bf(i):
        if F[i] != -1:
            return F[i]
        if i == 0:
            F[i] = A[0]
            return F[i]
        if i == 1:
            F[i] = max(A[0], A[1])
            return F[i]
        F[i] = max(bf(i-1), bf(i-2) + A[i])
        return F[i]
    return bf(i)


def ite_blackforest(A, i):
    n = len(A)

    a = A[0]
    b = A[1]
    c = -1
    if i == 0:
        return A[i]
    if i == 1:
        return max(A[0], A[1])
    for k in range(2, n):
        c = max(b, a + A[k])
        a = b
        b = c
    return c



if __name__ == '__main__':
    A = [1, 7, 5, 1, 4, 2, 1]
    print(mem_blackforest(A, len(A)-1))
