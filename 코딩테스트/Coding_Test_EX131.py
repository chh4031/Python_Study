def solution(num_list):
    result = -1
    for i in num_list:
        if i < 0:
            result = num_list.index(i)
            break
    if result == -1:
        return -1
    else:
        return result


print(solution([-1, 0, -2]))