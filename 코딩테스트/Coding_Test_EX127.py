def solution(my_string, target):
    if my_string.find(target) != -1:
        return 1
    else:
        return 0

print(solution("banana", "n"))