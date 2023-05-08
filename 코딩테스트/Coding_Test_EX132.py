def solution(strArr):
    result = []
    for i in strArr:
        if strArr.index(i) % 2 == 0:
            result.append(i.lower())
        else:
            result.append(i.upper())
    return result

print(solution(["AAA","BBB","CCC","DDD"]))