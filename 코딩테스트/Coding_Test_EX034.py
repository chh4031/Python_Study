def solution(str):
    arr = []
    result = []
    g = ""
    for i in str:
        arr.append(i)
    for i in range(len(arr)):
        k = arr.pop()
        result.append(k)
    for i in result:
        g += i
    print(g)
solution("abc")