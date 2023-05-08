def solution(arr):
    X = []
    for i in arr:
        for k in range(i):
            X.append(i)
    return X

print(solution([5, 1, 4]))