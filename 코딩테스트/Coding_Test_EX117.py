def solution(my_string, n):
    k = len(my_string) - n
    return my_string[k:]
print(solution("ProgrammerS123", 11))