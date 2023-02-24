from collections import deque

n, m = map(int, input().split())
graph = []
for i in range(n):
    graph.append(list(map(int, input())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
# 좌표문제에서 항상 나오는 좌표 설정

def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    while queue:
        print(queue)
        x, y = queue.popleft()
        # 이거는 x, y 값을 popleft 하는거임.
        print(x, y)
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            # 값 넘어가는지 체크
            if graph[nx][ny] == 0:
                continue
            # 괴물이 있는 곳(0)인 경우 체크
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))
                # append라서 뒤로 들어감. 그리고 그 이전 좌표 의 값도 달라질수 있는데 실제 결과값에는 영향을 미치지 않으므로 상관없음.
    return graph[n - 1][m - 1]
# 그래프의 마지막 좌표에 해당하는 값을 이용해서 구함.

print(bfs(0, 0))
# 실제 표를 그려서 이해하면 도움이 됨. 아래 표 참고
# 큐를 이용해서 실제 구현함.

"""
n = 3, m = 3

110
010
011

(0, 0) 3 (0, 1) 2 (0, 2) 0
(1, 0) 0  (1, 1) 3  (1, 2) 0
(2, 0) 0 (2, 1) 4 (2, 2) 5
"""