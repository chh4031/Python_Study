n, m, k = map(int, input().split()) # 공백 구분해서 기본 데이터 입력
# n은 배열 크기, m은 더하는 숫자의 총 갯수, k는 연속해서 더할 수 있는 최대 갯수
data = list(map(int, input().split())) # 공백 구분해서 리스트 형 데이터 입력

data.sort()
first = data[n-1] # 가장 큰수
second = data[n-2] # 두번째로 큰수

result = 0

while True:
    for i in range(k): # 가장 큰 수를 k번 더하는것
        if m == 0:
            break # m의 값이 0이 되면 탈출
        result += first
        m -= 1
    if m == 0:
        break
    result += second # 두번째로 큰수 더하기
    m -= 1

print(result)

# 이 문제는 사실상 가장 큰 수를 구하기 때문에 첫번째로 큰 수와 두번째로 큰 수만 필요함을 알 수 있다.