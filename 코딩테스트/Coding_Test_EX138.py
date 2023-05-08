def solution(arr, n):
    count = 0
    result = []
    if len(arr) % 2 == 0:
        for i in arr:
            if count == 0:
                result.append(i)
                count = 1
            else:
                result.append(i+n)
                count = 0
        return result
    else:
        for i in arr:
            if count == 0:
                result.append(i+n)
                count = 1
            else:
                result.append(i)
                count = 0
        return result
            
print(solution([49, 12, 100, 276, 33], 27))