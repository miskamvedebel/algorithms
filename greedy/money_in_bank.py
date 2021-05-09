def money_in_bank(n):
    '''returns money in bank after n days. considering mondays
    '''
    if n <= 1:
        return n
    total = 1
    prev = 1
    for i in range(2, n + 1):
        if i % 7 == 1:
            prev = i // 7
        curr = prev + 1
        total += curr
        prev = curr
    
    return total