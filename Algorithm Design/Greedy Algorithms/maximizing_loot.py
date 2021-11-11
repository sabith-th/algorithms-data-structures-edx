# Uses python3


def best_item(weights, values, n):
    maxValuePerWeight = 0
    bestItem = 0
    for i in range(n):
        if (weights[i] > 0):
            if ((values[i] / weights[i]) > maxValuePerWeight):
                maxValuePerWeight = values[i] / weights[i]
                bestItem = i
    return bestItem


def knapsack(W, weights, values, n):
    totalValue = 0
    for _ in range(n):
        if W == 0:
            return totalValue
        i = best_item(weights, values, n)
        a = min(weights[i], W)
        totalValue = totalValue + (a * (values[i] / weights[i]))
        weights[i] = weights[i] - a
        W = W - a
    return totalValue


if __name__ == '__main__':
    inp = open("3_2_loot.in", "r")
    values, weights = [], []
    n, k_weight = [int(i) for i in inp.readline().split()]
    for line in inp:
        if line == '\n':
            break
        val, weight = [int(i) for i in line.split()]
        values.append(val)
        weights.append(weight)
    inp.close()
    print(knapsack(k_weight, weights, values, n))
