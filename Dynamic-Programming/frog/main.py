from math import inf


def zaba_rek(road, i, energy):
    if i >= len(road)-1:
        return 0

    minn = inf
    if i + energy > len(road)-1:
        energy_loop = len(road)-1 - i
    else:
        energy_loop = energy
    for k in range(1, energy_loop + 1):
        res = zaba_rek(road, i + k, energy - k + road[i + k]) + 1
        minn = min(res, minn)
    return minn


def zaba_memo(road):
    lookup = [[-1 for _ in range(sum(road) + 1)] for _ in range(len(road))]

    def rek(i, energy):
        if i >= len(road)-1:
            return 0

        if lookup[i][energy] != -1:
            return lookup[i][energy]

        minn = inf
        for k in range(1, energy + 1):
            res = rek(i + k, energy - k + road[i + k]) + 1
            minn = min(res, minn)
        lookup[i][energy] = minn
        return lookup[i][energy]

    r = rek(0, road[0])
    return r


droga = [2, 0, 3, 1, 2]
# print(zaba_rek(droga, 0, droga[0]))
result = zaba_rek(droga, 0, droga[0])
print(result)