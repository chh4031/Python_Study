def solution(sides):
    sides.sort()
    k = sides.pop()
    if k >= (sides[0] + sides[1]):
        return 2
    else:
        return 1

print(solution([1,2,3]))