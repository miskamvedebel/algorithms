'''1725. Number Of Rectangles That Can Form The Largest Square
'''

def num_max_sqaures(rectangles: list) -> int:
    '''O(n) going thru the list of the rectangles and counting the numbers
    '''
    h = dict()
    mx = 0
    for r in rectangles:
        square_lenght = min(r)
        if not square_lenght in h:
            h[square_lenght] = 0
        h[square_lenght] += 1
        mx = max(mx, square_lenght)
    
    return h[mx]

if __name__ == '__main__':

    print('Should print 3')
    print(num_max_sqaures([[3, 5], [16, 3], [3, 1], [4, 3]]))