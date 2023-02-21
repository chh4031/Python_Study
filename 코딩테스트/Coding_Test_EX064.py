def solution(str):
    result = []
    for i in str:
        if i.isdigit():
            result.append(int(i))
    result.sort()
    return result
solution("123sfsf3r4")