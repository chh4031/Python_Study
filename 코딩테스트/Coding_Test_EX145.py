def solution(numbers, n):
    result = 0
    for i in numbers:
        if result > n:
            return result
        else:
            result += i
    return result


print(solution([34, 5, 71, 29, 100, 34], 123))