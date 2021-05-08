'''
Given a m x n matrix mat and an integer k, return a matrix answer where each answer[i][j] is the sum of all elements mat[r][c] for:

i - k <= r <= i + k,
j - k <= c <= j + k, and
(r, c) is a valid position in the matrix.
'''

def slow_block_sum(mat: list, K: int) -> list:
    '''Receives matrix and returns matrix of the same size with block sums
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

if __name__ == '__main__':
    mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    K = 1
    print(slow_block_sum(mat, K))