def last_stone(stones: list) -> int:
    #1046. Last Stone Weight
    stones.sort() # O(nlogn)
    
    while len(stones) > 1:
        y, x = stones.pop(), stones.pop()
        if x != y:
            stones.append(y - x)
            stones.sort()
    return stones.pop() if stones else 0

if __name__ == '__main__':
    
    assert last_stone([2,7,4,1,8,1]) == 1
    assert last_stone([1]) == 1
    assert last_stone([8, 8]) == 0
    assert last_stone([]) == 0