def min_cost(cost: [int]):

    n = len(cost) + 1
    tab = [0] * n

    for i in range(2, n):
        tab[i] = min(tab[i-1] + cost[i-1], tab[i-2] + cost[i-2])
    
    return tab[-1]

if __name__ == '__main__':

    assert min_cost([1, 10, 20, 15]) == 21
    assert min_cost([1,100,1,1,1,100,1,1,100,1]) == 6

    cost = list(map(lambda x: int(x), input().split()))
    print(f'Min cost {min_cost(cost)}')