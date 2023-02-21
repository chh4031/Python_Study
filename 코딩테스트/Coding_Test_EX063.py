def solution(sTr):
    result = ""
    for i in sTr:
        if i.isupper():
            result += i.lower()
        else:
            result += i.upper()
    return result

solution("saSsdfaSADf")