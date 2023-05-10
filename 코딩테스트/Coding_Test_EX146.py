def solution(n, k):
    result = []
    for i in range(k, n+1, k):
        result.append(i)
    return result

print(solution(11, 3))