def solution(n):
    result = []
    for i in range(1, n+1):
        if n % i == 0:
            result.append(i)
            result.append(n // i)
    result = list(set(result))
    result.sort()
    return result
solution(10000)