# 필요한 공식에 대한 설명
# n!/(n-m)! * m!

def solution(n, m):
    num1 = [i for i in range(n, 0, -1)]
    num2 = [i for i in range(m, 0, -1)]
    num3 = [i for i in range(n-m, 0, -1)]
    ex1 = 1
    ex2 = 1
    ex3 = 1
    for i in num1:
        ex1 *= i
    for k in num2:
        ex2 *= k
    for g in num3:
        ex3 *= g
    result = ex1 // (ex3 * ex2)
    return result
solution(5, 3)