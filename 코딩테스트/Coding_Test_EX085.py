def solution(array, n):
    arrayR = [i for i in array]
    arrayR.sort()
    result = n
    for i in arrayR:
        if abs(i - n) < result:
            result = abs(i - n)
            k = i
        else:
            pass
    return k

solution([3, 10, 12, 28], 20)