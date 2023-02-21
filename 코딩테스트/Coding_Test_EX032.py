def solution(n, k):
    sum = n * 12000 + k * 2000
    g = n // 10
    sum -= (g * 2000)
    return round(sum)