from math import inf


def cex(coins, index, value):
    if value == 0:
        return 0
    if value < 0 or index < 0:
        return inf
    return min(cex(coins, index, value-coins[index])+1, cex(coins, index-1, value))


def memo_cex(coins, index, value):
    F = [[None for _ in range(value+1)] for _ in range(len(coins))]

    def inside_memo_cex(index, value):
        if value < 0 or index < 0:
            return inf
        if F[index][value] is not None:
            return F[index][value]
        if value == 0:
            F[index][value] = 0
            return F[index][value]
        F[index][value] = min(inside_memo_cex(index, value-coins[index])+1, inside_memo_cex(index-1, value))
        return F[index][value]
    return inside_memo_cex(index, value)


if __name__ == '__main__':
    coins = [1, 3, 4]
    value = 6
    print(memo_cex(coins, len(coins)-1, value))
