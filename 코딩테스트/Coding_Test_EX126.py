def solution(num_list):
    result = 0
    if len(num_list) >= 11:
        for i in num_list:
            result += i
        return result
    else:
        result = 1
        for i in num_list:
            result *= i
        return result

print(solution([3, 4, 5, 2, 5, 4, 6, 7, 3, 7, 2, 2, 1]))