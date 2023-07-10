def solution(myString):
    answer = myString.split("x")
    result = []
    for i in answer:
        result.append(len(i))
    return result

print(solution("oxooxoxxox"))