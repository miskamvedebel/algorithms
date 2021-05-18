def happy_number(n: int) -> int:
    '''if ends up with 1 then happy
    '''
    processed = dict()
    
    def square(n):
        if n not in processed:
            processed[n] = sum([int(x) ** 2 for x in str(n)])
        else:
            return -1
        return processed[n]
    
    while n > 1:
        n = square(n)
    
    return n == 1

if __name__ == '__main__':
    assert happy_number(19) == True
    assert happy_number(2) == False
    assert happy_number(109) == True
    assert happy_number(1) == True