def solution(my_string):
    result = []
    for i in my_string.lower():
        result.append(i)
    result.sort()
    return ''.join(i for i in result)

solution("Bcad")