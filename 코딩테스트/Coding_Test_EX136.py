def solution(num_str):
    arr = [i for i in num_str]
    result = 0
    for i in arr:
        result += int(i)
    return result

print(solution("123456789"))