def solution(s):
    newList = [a for a in s]
    countList = list(''.join(set(newList)))
    result = []
    for i in countList:
        if (newList.count(i)) == 1:
            result.append(i)
    result.sort()
    result = ''.join(result)
    return result
solution("abcabcadc")