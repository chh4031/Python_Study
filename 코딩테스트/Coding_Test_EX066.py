def solution(n, numlist):
    result = numlist[:]
    for i in numlist:
        if i % n != 0:
            result.remove(i)
    return result
solution(3, [4, 5, 6, 7, 8, 9, 10, 11, 12])