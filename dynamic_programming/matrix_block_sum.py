import random
'''
Given a m x n matrix mat and an integer k, return a matrix answer where each answer[i][j] is the sum of all elements mat[r][c] for:

i - k <= r <= i + k,
j - k <= c <= j + k, and
(r, c) is a valid position in the matrix.
'''

def slow_block_sum(mat: list, K: int) -> list:
    '''Receives matrix and returns matrix of the same size with block sums
    Worst case O(n^4)
    '''

    m, n = len(mat), len(mat[0])
    tab = [[0] * n for _ in range(m)]
    for i in range(m):
        for j in range(n):
            r = max(0, i - K), min(i + K, m - 1)
            c = max(0, j - K), min(j + K, m - 1)

            for ii in range(r[0], r[1] + 1):
                for jj in range(c[0], c[1] + 1):
                    tab[i][j] += mat[ii][jj]
    return tab

def dp_block_sum(mat: list, K: int) -> list:
    '''Using dynamic programming
    '''
    m, n = len(mat), len(mat[0])
    tab = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            tab[i][j] = mat[i-1][j-1] + tab[i-1][j]  + tab[i][j-1] - tab[i-1][j-1]

    ans = mat.copy()

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            r = max(i - K - 1, 0), min(i + K, m)
            c = max(j - K - 1, 0), min(j + K, n)
            ans[i-1][j-1] = tab[r[1]][c[1]] + tab[r[0]][c[0]] - tab[r[0]][c[1]] - tab[r[1]][c[0]]
    
    return ans

if __name__ == '__main__':
    mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    K = 1
    print(slow_block_sum(mat, K))
    print(dp_block_sum(mat, K))