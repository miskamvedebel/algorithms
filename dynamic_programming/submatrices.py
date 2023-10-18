#1277. Count Square Submatrices with All Ones: https://leetcode.com/problems/count-square-submatrices-with-all-ones/
import numpy as np

def find_submatrices(matrix: list[list]) -> int:
    
    rows = len(matrix)
    cols = len(matrix[0])
    max_len = min(rows, cols)
    temp = []
    arr = np.array(matrix)
    res = 0

    for radius in range(1, max_len + 1):

        for r in range(rows):
            for c in range(cols):
                if r + radius <= rows and c + radius <= cols:
                    temp.append(arr[r:r+radius, c:c+radius])

    for t in temp:
        if t.sum() / (t.shape[0] * t.shape[1]) == 1.:
            res += 1
    return res

if __name__ == '__main__':
    print(find_submatrices([
  [1,0,1],
  [1,1,0],
  [1,1,0]
]
))
