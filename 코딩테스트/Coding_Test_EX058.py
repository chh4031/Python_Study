def solution(myString):
    arr = []
    result = ""
    for i in myString:
        arr.append(i)
    a = arr.count("a")
    for k in range(a):
        arr.remove("a")
    e = arr.count("e")
    for k in range(e):
        arr.remove("e")
    i = arr.count("i")
    for k in range(i):
        arr.remove("i")
    o = arr.count("o")
    for k in range(o):
        arr.remove("o")
    u = arr.count("u")
    for k in range(u):
        arr.remove("u")
    for k in arr:
        result += k
    return result
solution("nice to meet you")