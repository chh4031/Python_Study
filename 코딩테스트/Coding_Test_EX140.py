def solution(num_list, n):
    result = []
    for i in range(0, len(num_list), n):
        result.append(num_list[i])
    return result

print(solution([4, 2, 6, 1, 7, 6], 2))