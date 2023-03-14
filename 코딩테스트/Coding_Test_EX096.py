import re

def solution(numbers):
    numArray = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    count = 0
    recount = "0"
    result = numbers
    coll = ""
    for i in numArray:
        recount = str(count)
        result = result.replace(i, recount)
        count += 1
    coll = ''.join(re.findall(r"\d+", result))
    return int(coll)
print(solution("onefourzerosixseven"))