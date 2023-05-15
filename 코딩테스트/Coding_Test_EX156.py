def solution(str1, str2):
    result = ""
    for i in range(len(str1)):
        result += str1[i]
        result += str2[i]
    return result
print(solution("aaaaa", "12345"))