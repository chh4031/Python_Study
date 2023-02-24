# 그래프의 인접 리스트 방식을 append()함수를 사용하여 표현함
graph = [[] for _ in range(3)]

#  0번 노드에 저장된 정보
graph[0].append((1, 7))
graph[0].append((2, 5))

# 1번 노드에 저장된 정보
graph[1].append((0, 7))

# 2번 노드에 저장된 정보
graph[2].append((0, 5))

print(graph)