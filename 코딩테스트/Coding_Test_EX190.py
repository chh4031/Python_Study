def solution(order):
    result = 0
    for i in order:
        if "cafe" in i:
            result += 5000
        elif "am" in i:
            result += 4500
        else:
            result += 4500
    return result

print(solution(["cafelatte", "americanoice", "hotcafelatte", "anything"]))