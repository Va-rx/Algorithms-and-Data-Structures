def knapsack(W, P, H, BASIC_HEIGHT, BASIC_WEIGHT):
    n = len(W)
    F = [[[0 for height in range(BASIC_HEIGHT + 1)] for weight in range(BASIC_WEIGHT + 1)] for item in range(n)]
    #  F[item][weight][height]
    for weight in range(W[0], BASIC_WEIGHT + 1):
        for height in range(H[0], BASIC_HEIGHT + 1):
            F[0][weight][height] = P[0]

    for item in range(1, n):
        for weight in range(1, BASIC_WEIGHT + 1):
            for height in range(1, BASIC_HEIGHT + 1):
                F[item][weight][height] = F[item-1][weight][height]

                if weight-W[item] >= 0 and height-H[item] >= 0:
                    F[item][weight][height] = max(F[item][weight][height],
                                                F[item-1][weight-W[item]][height-H[item]] + P[item])
    return F[n-1][BASIC_WEIGHT][BASIC_HEIGHT]


if __name__ == '__main__':
    W = [10, 5, 2, 2, 7]  # weights
    P = [20, 3, 6, 8, 2]  # prices
    H = [2, 3, 3, 1, 1]  # heights
    BASIC_HEIGHT = 4
    BASIC_WEIGHT = 15

    result = knapsack(W, P, H, BASIC_HEIGHT, BASIC_WEIGHT)
    print(result)




