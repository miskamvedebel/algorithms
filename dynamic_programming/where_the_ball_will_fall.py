def find_ball(grid: list):
    '''
    Solution for the problem of falling ball
    '''
    
    MAP = {(0, 1): "left", (1, 0): "up", (-1, 0): "down", (0, -1): "right"}
    rows = len(grid)
    columns = len(grid[0])

    # if it's just of the size 1 - then we return the answer straight away
    if rows == 1 and columns == 1:
        return [-1]

    results = []

    for col in range(columns):
        R, C = 0, col
        direction = "up"
        r, c = R, C
        res = -1
        while True:
            value = grid[r][c]
            if direction == "up":
                c += value
            if direction == "left":
                r += value
            if direction == "right":
                r -= value

            if c > columns - 1 or c < 0:
                break
            if r < 0:
                break
            if r > rows - 1:
                res = c
                break
            direction = MAP.get((r-R, c-C))
            R, C = r, c
            if direction == "down":
                break   
        
        results.append(res)

    return results

if __name__ == '__main__':
    assert find_ball(grid=[[-1]]) == [-1]
    assert find_ball(grid=[[1]]) == [-1]
    assert find_ball(grid=[[1, 1]]) == [1, -1]

    print(find_ball(grid=[[1,1,1,-1,-1],[1,1,1,-1,-1],[-1,-1,-1,1,1],[1,1,1,1,-1],[-1,-1,-1,-1,-1]]))
    print(find_ball(grid=[[1,1,1,1,1,1],[-1,-1,-1,-1,-1,-1],[1,1,1,1,1,1],[-1,-1,-1,-1,-1,-1]]))
    print(find_ball(grid=[[1, 1, -1, 1], [1, 1, -1, -1]]))