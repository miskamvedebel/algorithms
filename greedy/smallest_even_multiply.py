from cgitb import small


def smallest_even_multiply(n: int) -> int:
    '''Function that returns smallest even mulpiply of n (2413)
    
    :param n: Integer number
    :type n: int 

    :returns: integer number that is a minimum even multiply
    :rtype: int
    '''
    if n% 2 == 0:
            return n
    return n * 2

if __name__ == "__main__":

    assert smallest_even_multiply(n=2) == 2
    assert smallest_even_multiply(n=5) == 10
    assert smallest_even_multiply(n=10) == 10
    assert smallest_even_multiply(n=23) == 46
