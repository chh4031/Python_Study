def solution(myString):
    myList = [i for i in myString]
    result = []
    resultString=""
    for i in myList:
        if i not in result:
            result.append(i)
    for i in result:
        resultString += i
    return resultString


solution("We are the world"	)