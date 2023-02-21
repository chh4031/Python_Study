def solution(n):
    k = 0
    for i in range(1, n+1, 1):
        if (i * i) == n:
            k = 1
            break
        else:
            k = 2
    return k
print(solution(976))