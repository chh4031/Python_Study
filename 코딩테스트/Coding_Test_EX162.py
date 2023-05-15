def solution(arr):
    count = 0
    for i in range(len(arr)):
        for k in range(len(arr)):
            if arr[i][k] == arr[k][i]:
                pass
            else:
                count += 1
    if count != 0:
        return 0
    else:
        return 1


print(solution([[5, 192, 33], [192, 72, 95], [33, 95, 999]]))