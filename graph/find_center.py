def find_center(edges: list) -> int:
    graph = {}
    for edge in edges:
        x, y = edge
        if x not in graph:
            graph[x] = 0
        if y not in graph:
            graph[y] = 0
        graph[x] += 1
        graph[y] += 1
    
    return sorted(graph.items(), key=lambda x: x[1], reverse=True)[0][0]

if __name__ == '__main__':
    print(find_center([[1,2],[2,3],[4,2]]))
    print(find_center([[1,2],[5,1],[1,3],[1,4]]))