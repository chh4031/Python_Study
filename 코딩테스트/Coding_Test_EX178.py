def solution(arr, idx):
    result = arr[idx:]
    result1 = arr[:idx]
    try:
        indexNum = result.index(1)
    except:
        return -1
    return indexNum + len(result1)

print(solution([0,0,0,1], 1))