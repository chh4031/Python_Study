def solution(n):
    m = n
    result = [n]
    while(m != 1):
        if m % 2 == 0:
            m //= 2
            result.append(m)
        elif m % 2 != 0:
            m = m * 3 + 1
            result.append(m)
    return result
        

print(solution(10))