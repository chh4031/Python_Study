def solution(num_list):
    result = []
    for i in range(len(num_list)):
        k = num_list.pop()
        result.append(k)
    return result
solution([1, 2, 3, 4, 5])