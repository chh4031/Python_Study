def solution(myString):
    result = ""
    for i in myString:
        if "l" < i:
            result += i
        else:
            result += "l"
    return result
print(solution("abcdevwxyz"))