def solution(n):
    result = []
    for i in range(1, n+1):
        count = 0
        for k in range(1, i+1):
            if i % k == 0:
                count += 1
        if count == 2:
            result.append(i)
    return n - (len(result) +1 )
solution(10)