def solution(box, n):
    result = 1
    k = 0
    for i in box:
        k = i // n
        result *= k
    return result
solution([10, 8, 6], 3)