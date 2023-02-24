n, m = map(int, input().split())
# 전체 맵 좌표 n:행, m:열

d = [[0]*m for _ in range(n)]
print(d)
# 각 맵 좌표에 0으로 초기화
x, y, direction = map(int, input().split())
# 캐릭터 좌표 설정
d[x][y] = 1
# 현재 캐릭터가 위치한 좌표값을 1으로 설정, 이유는 이미 방문한 좌표이기에 

array = []
for i in range(n):
    array.append(list(map(int, input().split())))
# 맵 정보를 입력하는 구문. 행 만큼 입력하게 설정

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
# 각 북 동 남 서 방향 정의

def turnLeft():
    global direction # 전역함수로 쓰기 위해 global로 선언
    direction -= 1
    if direction == -1:
        direction = 3
# 왼쪽으로 회전시키는 함수를 선언

# 아래코드는 시뮬레이션을 위한 코드
count = 1
turn_time = 0 # 각 좌표가 막혔는지 확인하는 코드
while True:
    turnLeft()
    nx = x + dx[direction]
    ny = y + dy[direction]

    if d[nx][ny] == 0 and array[nx][ny] == 0:
        d[nx][ny] = 1
        x = nx
        y = ny
        count += 1
        turn_time = 0
        continue
    # 회전이후 가보지 않은 칸인 경우 이동하는 코드
    else:
        turn_time += 1
    # 회전 이후 막혔거나 가본 칸인 경우

    # 전 방향이 전부 막힌 경우
    if turn_time == 4:
        nx = x - dx[direction]
        ny = y - dy[direction]

        # 뒤로 가는 것이 가능하면 뒤로 이동
        if array[nx][ny] == 0:
            x = nx
            y = ny
        else:
            break
        # 뒤가 막힌 경우
        turn_time = 0
print(count)

# 캐릭터가 방문한 칸의 수를 구하는 시뮬레이션 문제이다. 난이도가 좀 있음.