import re

def solution(myString):
    result = 0
    newList = re.findall(r'\d+', myString)
    # finall은 조건에 맞는 것을 리스트형식으로 반환해줌
    # \d+는 숫자로 나열시키는데 연속되면 연속시킨것도 같이 반환
    for i in newList:
        result += int(i)
    return result
solution("1a2b3c4d123Z")