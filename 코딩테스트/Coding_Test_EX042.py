def solution(myString, letter):
    newArr = []
    result = ""
    for i in myString:
        newArr.append(i)
    for i in range(newArr.count(letter)):
        newArr.remove(letter)
    for i in newArr:
        result += i
    return result

solution("abcdefg", "f")