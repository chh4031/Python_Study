# 행 = n, 열 = m
# min함수를 이용해 구현함 식
# 조건은 행에서 가장 작은 수를 뽑는데 승리하려면 각 행에서 가장 작은 수중 큰 것을 골라야 한다.
n, m = map(int, input().split())
result = 0

for i in range(n):
    data = list(map(int, input().split()))
    # 각 행을 입력
    min_value = min(data)
    # 각 행에서 가장 작은 데이터를 뽑아옴
    result = max(result, min_value)
    # 두 인자를 비교해서 가장 큰 수를 반환
print(result)
