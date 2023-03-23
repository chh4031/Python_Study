def solution(num_list):
    count = 0
    answer = []
    for i in num_list:
        for k in range(2, i+1):
            if i == 2:
                break
            count += 1
            if i % k == 0:
                break
        if i == 2:
            answer.append(True)
        elif i == count+1:
            answer.append(True)
        else:
            answer.append(False)
        count = 0
    return answer

print(solution([2, 3, 4, 5, 6, 7, 8, 9]))