n, m = map(int, input().split())

graph = []
for i in range(n):
    graph.append(list(map(int, input())))
print(graph)

def dfs(x, y):
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False
    if graph[x][y] == 0:
        graph[x][y] = 1
        dfs(x - 1, y)
        dfs(x, y - 1)
        dfs(x + 1, y)
        dfs(x, y + 1)
        return True
    return False

result = 0
for i in range(n):
    for j in range(m):
        if dfs(i, j) == True:
            result += 1
print(result)

# 재귀로 돌아가는 것만 기억해서 하면됨.
# 재귀부분 True 왜 있나 싶을건데 재귀 돌아가는 부분에서 돌아간 재귀함수의 리턴값은 큰 상관이 없고, 방문지점 0 1 체크하는 용도로만 쓰임.
# 각 상하좌우에 해당하는 dfs 연산을 완료했으면 리턴 True를 반환해서 result 값이 1 올라감.