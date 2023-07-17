def solution(arr, queries):
    for i in queries:
        for k in range(i[0], i[1]+1):
            arr[k] = arr[k] + 1
            print(k)
    return arr

print(solution([0, 1, 2, 3, 4], [[0,1], [1,2], [2,3]]))