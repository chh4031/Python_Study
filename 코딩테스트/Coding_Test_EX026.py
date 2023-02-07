def solution(left, right):
    arr1 = []
    result = 0
    for i in range(left, right+1):
        arr1.append(i)
    for k in arr1:
        if int(k ** (1/2)) ** 2 == k:
            result -= k
        else:
            result += k
    print(result)
solution(24, 27)