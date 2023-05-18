def solution(strArr):
    result = []
    for i in strArr:
        if "ad" in i:
            pass
        else:
            result.append(i)
    return result


print(solution(["and","notad","abcd"]))