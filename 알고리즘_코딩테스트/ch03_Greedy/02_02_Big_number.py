# 더 효율적인 계산을 위한 개선식
# 반복되는 수열에 따라 계산식이 달라진다.
# 도출될 수 있는 식은 int(M/(K+1) * K + M % (K + 1))

n, m, k = map(int, input().split())
data = list(map(int, input().split()))

data.sort()
first = data[n-1]
second = data[n-2]

count = int(m/(k+1)) * k # 가장 큰 수가 더해지는 횟수
count += m % (k+1) # m으로 나누어 떨어지지 않는 경우에 또 더해질 수 있는 큰수의 횟수

result = 0
result += (count) * first # 큰수만 더하기
result += (m-count) * second # 두번재로 큰수 더하기

print(result)