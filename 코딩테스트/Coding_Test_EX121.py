def solution(myString, pat):
    newArr = []
    for i in myString:
        if i == "A":
            newArr.append("B")
        else:
            newArr.append("A")
    newString = ''.join(newArr)
    if newString.find(pat) == -1:
        return 0
    else:
        return 1
print(solution("ABBAA", "AABB"))