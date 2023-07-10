def solution(a, d, included):
    result = []
    answer = 0
    num = a
    for i in range(len(included)):
        result.append(num)
        num += d
    for k in range(len(included)):
        if included[k] == True:
            answer += result[k]
    return answer

print(solution(3, 4, [True, False, False, True, True]))