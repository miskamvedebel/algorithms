def strictly_palindromic(n: int) -> bool:
    '''2396. Strictly Palindromic Number

    :param n: integer to check
    :type n: in
    :returns: answer - true or false
    :rtype: bool
    '''

    MAX_BASE = n - 2
    checks = []
    if MAX_BASE < 2:
        return False
    for b in range(2, MAX_BASE + 1):
        t = []
        