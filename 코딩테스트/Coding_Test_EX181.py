def solution(numLog):
    result = []
    for i in range(len(numLog)-1):
        if (numLog[i] + 1) == numLog[i+1]:
            result.append("w")
        elif (numLog[i] - 1) == numLog[i+1]:
            result.append("s")
        elif (numLog[i] + 10) == numLog[i+1]:
            result.append("d")
        else:
            result.append("a")
    resultString = ""
    for i in result:
        resultString += i
    return resultString

print(solution([0, 1, 0, 10, 0, 1, 0, 10, 0, -1, -2, -1]))