n, k = map(int, input().split())
result = 0

while n > k: # N이 K이상 이면 계속 K 나누기
    while n % k != 0: # N / K의 나머지가 0이 아니면 -1하기
        n -= 1
        result += 1
    n //= k # 정수형 나누기임
    result += 1

while n > 1: # 마지막으로 남은 수에 대해 1씩 빼기
    n -= 1
    result += 1

print(result)
