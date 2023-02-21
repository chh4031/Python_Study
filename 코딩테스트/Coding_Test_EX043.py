def solution(myString, n):
    result = ""
    for i in myString:
        result += i * n
    return result

solution("Hello", 3)