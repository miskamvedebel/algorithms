def water_bottles_queue(numBottles: int, numExchange: int) -> int:
    '''NOT OPTIMAL SOLUTION
    '''
    bottles = [1] * numBottles
    empty = 0
    total = 0
    while bottles:
        empty += bottles.pop()
        total += 1
        if empty == numExchange:
            bottles.append(1)
            empty = 0
    return total

if __name__ == '__main__':

    print(water_bottles_queue(9, 3)) # should print 13
    print(water_bottles_queue(9, 3) == 13)
