def solution(arr):
    newArr = []
    for i in arr:
        newArr.append(len(i))
    return newArr
solution(["We", "are", "the", "world!"])