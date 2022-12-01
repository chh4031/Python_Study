def solution(arr):
    arr.sort()
    if(len(arr) <= 1):
        return [-1]
    else:
        del arr[0]
        arr.reverse()
        return arr

print(solution([300, 3, 40]))