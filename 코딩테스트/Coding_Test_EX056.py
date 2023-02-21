import re

def solution(myString):
    result = 0
    numbers = re.sub(r'[^0-9]', '', myString)
    for i in numbers:
        result += int(i)
    return result
solution("aAb1B2cC34oOp")