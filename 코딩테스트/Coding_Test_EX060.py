def solution(n):
    s1 = n // 5
    s2 = (n % 5) // 3
    s3 = ((n % 5) % 3) // 1

    return s1+s2+s3
solution(999)