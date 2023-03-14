def solution(s):
    mysum = 0
    result = s.split(" ")
    for i in range(len(result)):
        if result[i] == "Z":
            mysum -= int(result[i-1])
        else:
            mysum += int(result[i])
    return mysum

print(solution("1 2 Z 3"))