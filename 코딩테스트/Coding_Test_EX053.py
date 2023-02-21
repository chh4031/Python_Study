def solution(arr):
    arr.sort()
    k = (len(arr) // 2)
    return arr[k]

solution([1,5,6,7,3])