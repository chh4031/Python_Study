def solution(myString):
    result = ""
    for i in myString:
        if i == "a" or i == "A":
            result += i.upper()
        else:
            result += i.lower()
    return result

print(solution("abstract algebra"))