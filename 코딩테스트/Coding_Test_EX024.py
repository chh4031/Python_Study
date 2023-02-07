def solution(a, b):
    i = 0
    result = 0
    while(i < len(a)):
        result += a[i] * b[i]
        i += 1
    print(result)
    return result

solution([1,2,3,4], [-3,-1,0,2])

"""
a[0]*b[0] + a[1]*b[1] + ... + a[n-1]*b[n-1]
"""