def moving_balls(boxes: str) -> list:
    n = len(boxes)
    res = [0] * n
    for i in range(n):
        for j in range(n):
            if i != j and boxes[j] == '1':
                res[i] += abs(i-j)
    return res

if __name__ == '__main__':
    assert moving_balls('110') == [1, 1, 3]
    assert moving_balls('001011') == [11, 8, 5, 4, 3, 4]
    assert moving_balls('1000001') == [6, 6, 6, 6, 6, 6, 6]