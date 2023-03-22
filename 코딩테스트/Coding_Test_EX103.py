def solution(dots):
    xdot = [dots[0] for dots in dots]
    ydot = [dots[1] for dots in dots]
    return (max(xdot) - min(xdot)) * (max(ydot) - min(ydot))
print(solution([[1, 1], [2, 1], [2, 2], [1, 2]]))

# 해당 문법식에서 dots[0] for dots in dots를 쓰면 배열의 0번째 단일항에 대해서만 반복을 수행한다.