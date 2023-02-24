# 이중 for문을 활용해서 가장 작은 수들 중 가장 큰 수 찾기
n, m = map(int, input().split())
result = 0

for i in range(n):
    data = list(map(int, input().split()))

    min_value = 1001
    for j in data:
        min_value = min(min_value, j)
    result = max(result, min_value)

print(result)