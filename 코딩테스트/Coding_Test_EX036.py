def solution(num_list):
    g = 0
    k = 0
    for i in num_list:
        if i % 2 == 0:
            g += 1
        else:
            k += 1
    new_list = [g, k]
    return new_list
print(solution([1,2,3,4,5]))
