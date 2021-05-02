def max_substring(a, b):
    '''
    :param a: first string
    :param b: second string
    
    :returns: max substring
    '''
    n = len(a) + 1
    m = len(b) + 1
    
    tab = [[0]*n for _ in range(m)]
    
    for i in range(1, m):
        for j in range(1, n):
            if a[j-1] == b[i-1]:
                tab[i][j] = tab[i-1][j-1] + 1

    ans = max([max(x) for x in tab])
                
    return ans

def max_rep_letters(a, b):
    '''
    :param a: first string
    :param b: second string

    :returns: number of rep letters
    '''

    n = len(a) + 1
    m = len(b) + 1

    tab = [[0]*n for _ in range(m)]

    for i in range(1, m):
        for j in range(1, n):
            if a[j-1] == b[i-1]:
                tab[i][j] = tab[i-1][j-1] + 1
            else:
                tab[i][j] = max(tab[i-1][j], tab[i][j-1])

    return tab[-1][-1]

if __name__ == '__main__':
    print("Max substring:")
    print("Fort and fosh")
    print(max_substring('fosh', 'fort'))

    print("Fosh and fish")
    print(max_substring('fosh', 'fish'))

    print("blue and clues")
    print(max_substring('blue', 'clues'))


    print("Number of letters:")
    print("Fort and fosh")
    print(max_rep_letters('fosh', 'fort'))

    print("Fosh and fish")
    print(max_rep_letters('fosh', 'fish'))
