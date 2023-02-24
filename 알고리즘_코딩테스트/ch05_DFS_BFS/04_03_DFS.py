def dfs(graph, v, visited):
    visited[v] = True
    print(v, end=' ')
    # print(visited)
    for i in graph[v]:
        if not visited[i]: # 이거 not이라서 값이 False일때 작동함.
            dfs(graph, i, visited)

graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]
# 각 노드 데이터는 1~8까지 적힌대로 인접 노드에 대한 리스트로 만듬 => 2차원 리스트로 구성함.

visited = [False] * 9
dfs(graph, 1, visited)

# 각 노드에 대한 탐색을 하고, 다시 돌아가서 탐색한다는 것만 알고 있으면 코드 쉽게 이해 가능