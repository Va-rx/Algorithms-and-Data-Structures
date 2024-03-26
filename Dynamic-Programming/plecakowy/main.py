

def find_solution():
    solution = []
    item_index = n-1
    weight_index = Weight
    while item_index > 0 and weight_index >= 0:
        if F[item_index][weight_index] != F[item_index-1][weight_index]:
            solution.append(item_index)
            weight_index -= W[item_index]
        item_index -= 1
    if item_index == 0 and F[item_index] != 0:
        solution.append(item_index)
    print(solution)



W = [31,
10,
20,
19,
 4,
 3,
 6]  # wagi
P = [70,
20,
39,
37,
 7,
 5,
10]  # ceny
n = len(W)
Weight = 50
List_Result = []
F = [[0 for _ in range(Weight + 1)] for _ in range(n)]
for i in range(W[0], Weight + 1):
    F[0][i] = P[0]

for i in range(1, Weight + 1):
    for j in range(1, n):
        F[j][i] = F[j-1][i]

        if i-W[j] >= 0:
            F[j][i] = max(F[j][i], F[j-1][i-W[j]] + P[j])
print(F[n-1][Weight])
find_solution()




