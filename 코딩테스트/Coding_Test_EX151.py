def solution(arr):
    result = []
    for i in arr:
        if (i >= 50) & (i % 2 == 0):
            result.append(i // 2)
        elif (i < 50) & (i % 2 != 0):
            result.append(i * 2)
        else:
            result.append(i)
    return result

print(solution([1, 2, 3, 100, 99, 98]))