def solution(mystring):
    result = mystring
    print(result)
    resultArray = result.split(' ')
    print(resultArray)
    answer = int(resultArray[0])
    for i in range(len(resultArray)):
        if resultArray[i] == "+":
            answer += int(resultArray[i+1])
        elif resultArray[i] == "-":
            answer -= int(resultArray[i+1])
    return answer

print(solution("30 + 40 - 30 + 10"))