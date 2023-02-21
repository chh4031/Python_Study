def solution(n):
    g = 0
    i = 0 
    if n <= 7:
        return 1
    else:
        g = n / 7
        if n % 7 != 0:
            g += 1
        return int(g)
print(solution(15))