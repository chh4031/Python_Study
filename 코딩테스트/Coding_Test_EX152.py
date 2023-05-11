def solution(num_list):
    controller = 0
    even = 0
    odd = 0
    for i in num_list:
        if controller == 0:
            odd += i
            controller = 1
        else:
            even += i
            controller = 0
    if even > odd:
        return even
    elif odd > even:
        return odd
    else:
        return even


print(solution([4, 2, 6, 1, 7, 6]))