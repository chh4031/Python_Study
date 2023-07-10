def solution(myString):
    result = myString.split('x')
    if "" in result:
        for i in range(result.count("")):
            result.remove("")
    result.sort()
    return result

print(solution("asdfxxdsfxxdsf"))