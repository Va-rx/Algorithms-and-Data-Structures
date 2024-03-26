from math import inf
# najdłuzszy rosnacy niespojny podciag (longest increasing subsequence)


def print_solution(A, P, i):
    if P[i] != -1:
        print_solution(A, P, P[i])
    print(A[i])


def lis(array):
    n = len(array)
    F = [1 for _ in range(n)]
    P = [-1 for _ in range(n)]
    for i in range(1, n):
        maxx = 1
        index = -1
        for j in range(i):
            if array[j] < array[i] and maxx <= F[j] + 1:
                maxx = F[j] + 1
                index = j
        F[i] = maxx
        P[i] = index
    return F, P


array = [2, 1, 4, 3, 1, 5, 2, 7, 8, 3]
f_array, p_array = lis(array)
last_index = 0
for i in range(len(array)):
    if f_array[i] == max(f_array):
        last_index = i

print_solution(array, p_array, last_index)
