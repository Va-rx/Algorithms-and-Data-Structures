def subset_sum(A, summ):
    n = len(A)
    F = [[False for _ in range(summ+1)] for _ in range(n+1)]
    for item in range(n+1):
        F[item][0] = True

    for item in range(1, n+1):
        for sum in range(1, summ+1):
            if sum-A[item-1] >= 0:
                F[item][sum] = F[item-1][sum] or F[item-1][sum-A[item-1]]
            else:
                F[item][sum] = F[item-1][sum]

    return F[n][summ]


if __name__ == '__main__':
    A = [2, 7, 3, 4]
    summ = 9
    result = subset_sum(A, summ)
    print(result)