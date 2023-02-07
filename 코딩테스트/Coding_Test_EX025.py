def solution(s):
    a = list(map(str, s))
    a.sort(reverse=True)
    b = ""
    for i in a:
        b += i
    print(b)
    return a

solution("Zbcdefg")