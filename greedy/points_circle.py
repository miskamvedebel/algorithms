def points_circle(points: list, queries: list) -> list:
    
    circle_equation = lambda x, y, h, k, r: (x - h) ** 2 + (y - k) ** 2 <= r ** 2
    res = []
    for h, k, r in queries:
        counter = 0
        for x, y in points:
            counter += circle_equation(x, y, h, k, r)
        res.append(counter)
    return res

if __name__ == '__main__':
    points = [[1,1],[2,2],[3,3],[4,4],[5,5]]
    queries = [[1,2,2],[2,2,2],[4,3,2],[4,3,3]]
    print(points_circle(points, queries))

    points = [[1,3],[3,3],[5,3],[2,2]]
    queries = [[2,3,1],[4,3,1],[1,1,2]]
    print(points_circle(points, queries))