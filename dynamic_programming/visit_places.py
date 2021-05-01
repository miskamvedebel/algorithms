def plan_visits(time, importance, stay):
    '''
    :param time: array of times required for the visit
    :param importance: array of importance of this place
    :param stay: duration of a stay in destination
    
    :returns: max value that could be achieved
    '''
    
    step = min(time)
    places = len(importance) + 1
    n = int(stay / step) + 1
    tab = [[0] * n for _ in range(places)]
    
    for i in range(1, places):
        for j in range(1, n):
            t, imp = time[i-1], importance[i-1]
            prev = tab[i-1][j]
            if t <= j * step:
                index = int((j * step - t) / step)
                tab[i][j] = max(prev, imp + tab[i-1][index])
            else:
                tab[i][j] = prev
    
    return tab

if __name__ == '__main__':
    w = [1/2, 1/2, 1, 2, 1/2]
    v = [7, 6, 9, 9, 8]
    stay = 2
    print(plan_visits(time=w, importance=v, stay=stay))