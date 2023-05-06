def solution(arr, k):
    arr1 = []
    if k % 2 == 0:
        arr1 = [i+k for i in arr]
    else:
        arr1 = [i*k for i in arr]
    return arr1
print(solution([1, 2, 3, 100, 99, 98], 2))