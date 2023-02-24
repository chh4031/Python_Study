from collections import deque

def bfs(graph, start, visited):
    queue = deque([start])
    # queue 자체는 deque로 만들어진 거임
    visited[start] = True
    # 방문처리하는부분
    while queue:
        # queue가 빌때까지하는데 헷갈릴수 있는게 밑에서 queue를 재정의해줘서 같은 값만 들어가서 도는 구조는 아님.
        v = queue.popleft()
        # 큐 특성을 이용해서 뒤에서 left시켜서 앞에서 꺼내줌
        print(v, end=' ')
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
                # for문에서 graph에 있는 값들을 큐로 하여 해줌.

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

visited = [False] * 9
bfs(graph, 1, visited)