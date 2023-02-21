def solution(myString, num1, num2):
    string = ""
    result = [i for i in myString]
    n1 = result[num1]
    n2 = result[num2]

    result[num1] = n2
    result[num2] = n1

    for i in result:
        string += i
    return string

solution("hello", 1, 2)