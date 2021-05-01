def knapsack(weight, values, capacity):
    '''
    :param weight: array of weights
    :param values: array of values
    :param capacity: capacity of knapsack

    :returns: max values that could be achieved

    '''

    items = len(weight) + 1
    ks = capacity + 1
    
    tab = [[0] * ks for _ in range(items)]

    for i in range(1, items):
        for j in range(1, ks):
            w, v = weight[i-1], values[i-1]
            prev = tab[i-1][j]
            if w <= j:
                tab[i][j] = max(prev, v + tab[i-1][j-w])
            else:
                tab[i][j] = prev

    return tab[-1][-1]

if __name__ == '__main__':

    weight = [4, 3, 1]
    values = [3000, 2000, 1500]
    cap = 4
    print(knapsack(weight=weight, values=values, capacity=cap))
    assert knapsack(weight=weight, values=values, capacity=cap) == 3500

    weight = [1, 3, 4]
    values = [1500, 2000, 3000]
    cap = 4
    print(knapsack(weight=weight, values=values, capacity=cap))
    assert knapsack(weight=weight, values=values, capacity=cap) == 3500

    weight = [1, 3, 4, 1]
    values = [1500, 2000, 3000, 2000]
    cap = 4
    print(knapsack(weight=weight, values=values, capacity=cap))
    assert knapsack(weight=weight, values=values, capacity=cap) == 4000

    weight = [1, 3, 4, 1, 1]
    values = [1500, 2000, 3000, 2000, 1000]
    cap = 4
    print(knapsack(weight=weight, values=values, capacity=cap))
    assert knapsack(weight=weight, values=values, capacity=cap) == 4500


