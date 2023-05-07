def solution(n, control):
    for i in control:
        if i == "w":
            n += 1
        elif i == "s":
            n -= 1
        elif i == "d":
            n += 10
        else:
            n -= 10
    return n

print(solution(0, "wsdawsdassw"))

"""
w = +1
s = -1
d = +10
a = -10
"""