def solution(a, n):
    result = 0
    resultArr = 0
    for i in n:
        for k in a:
            if k not in i:
                result -= 1
            elif i.count(k) == 1:
                result += 1
        if result == len(i):
            resultArr += 1
        result = 0
    if resultArr == 0:
        return 2
    else:
        return 1
print(solution(["s", "o", "m", "d"], ["moos", "dzx", "smm", "sunmmo", "som"]))