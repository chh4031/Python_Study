def solution(arr, flag):
    result = 0
    arrR = []
    for i in range(len(arr)):
        arrR.append(arr.find(flag, result))
        result=arr.find(flag, result)+1
    return arr[:max(arrR)+len(flag)]
print(solution("aaAAaAAA", "AA"))