n = int(input())

x, y = 1,1
plans = input().split()

dx = [0,0,-1,1]
dy = [-1,1,0,0]
moveType = ['L', 'R', 'U', 'D']

for plan in plans:
    for i in range(len(moveType)):
        if plan == moveType[i]:
            nx = x + dx[i]
            ny = y + dy[i]
    if nx < 1 or ny < 1 or nx > n or ny > n: # 이 부분이 지정좌표에서 벗어나는 경우를 의미하는것. 좌표값이 0이 없어야 하며, N 을 벗어나면 안됨.
        continue
    x, y = nx, ny

print(x,y)

# 입력값은 5 R R R U D D 일때 5은 N 값으로 크기를 정하는 것임. 1,1 ~ N, N 까지의 좌표가 있다고 가정하는것.
# R R R U D D는 각 좌표들의 이동을 구하는 것 U는 좌표를 벗어나는 경우임.
# 완전탐색 문제 유형