def backtrack_items(items, weight, values, capacity):
    '''Function to identify the items to be taken
    
    :param items: array of item names
    :param weight: array of weights of the items
    :param values: array of values of the items
    :param capacity: maximum capacity of the knapsack
    
    :returns: the list of items
    '''
    num_items = len(items) + 1
    ks = capacity + 1
    
    items_list = [[-1] * ks for _ in range(num_items)]
    included = [[False] * ks for _ in range(num_items)]
    tab = [[0] * ks for _ in range(num_items)]

    for i in range(1, num_items):
        for j in range(1, ks):
            w, v = weight[i-1], values[i-1]
            prev = tab[i-1][j]
            if w <= j:
                tab[i][j] = max(prev, v + tab[i-1][j-w])
                items_list[i][j] = (i-1, j-w) if tab[i][j] == v + tab[i-1][j-w] else (i-1, j)
                included[i][j] = True if tab[i][j] == v + tab[i-1][j-w] else False
            else:
                tab[i][j] = prev
                items_list[i][j] = (i-1, j)
                
    row, col = len(items_names), capacity
    total_value = tab[row][col]
    list_of_items = []

    while total_value > 0:
        if row == 0 or col == 0:
            break
        if included[row][col]:
            list_of_items.append(items[row-1])
            total_value -= values[row-1]
        row, col = items_list[row][col]
    
    return list_of_items


if __name__ == '__main__':
    items_names = ['water', 'book', 'food', 'coat', 'camera']
    weight = [3, 1, 2, 2, 1]
    values = [10, 3, 9, 5, 6]
    capacity = 6
    print(backtrack_items(items=items_names, weight=weight, values=values, capacity=capacity))