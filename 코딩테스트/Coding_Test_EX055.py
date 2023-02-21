def solution(n):
    k = str(n)
    result = 0
    for i in k:
        result += int(i)
    return result
solution(1234)