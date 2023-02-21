def solution(slice, n):
    k = 1
    sl = slice
    while True:
        g = sl * k
        if (g - n) >= 0:
            break
        else:
            k += 1
    return k
print(solution(2, 100))