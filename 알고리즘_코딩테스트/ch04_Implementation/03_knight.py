input_data = input()
row = int(input_data[1])
col = int(ord(input_data[0])) - int(ord('a')) + 1
# 데이터 값이 a1 b1 이런식으로 들어옴. 그래서 ord 함수로 유니코드 정수를 반환시켜서 새롭게 좌표를 만드는 기능

steps = [(-2,-1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]
# 이동가능한 좌표값을 지정한 것. 각 8개임

result = 0 
for step in steps:
    nR = row + step[0]
    nC = col + step[1]
    # 이동하고자 하는 좌표를 생성
    if nR >= 1 and nR <= 8 and nC >= 1 and nC <= 8:
        result += 1
    # 범위는 8, 8로 지정되어 있기 때문에 해당 좌표를 벗어나는 것은 스킵해야함. 해당 조건을 추가시킨것.
print(result)

# 완전탐색 문제 유형