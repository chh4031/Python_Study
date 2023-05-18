def solution(a, b, c):
    if a == b and a == c and b == c:
        return (a + b + c) * (a**2 + b**2 + c**2) * (a**3 + b**3 + c**3)
    elif a != b and a != c and b != c:
        return (a + b + c)
    else:
        return (a + b + c) * (a**2 + b**2 + c**2)

print(solution(2, 6, 1))