import re

def solution(numbers):
    numArray = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "zero"]
    newNumbers = numbers
    count = 0
    recount = "0"
    result = ""
    coll = ""
    for i in numArray:
        recount = str(count)
        result += newNumbers.replace(i, recount)
        count += 1
    coll = ''.join(re.findall(r"\d+", result))
    return coll
solution("onefourzerosixseven")