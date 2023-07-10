def solution(a, b):
    result1 = int(str(a) + str(b))
    result2 = 2 * a * b
    if result1 > result2:
        return result1
    else:
        return result2

print(solution(2, 91))