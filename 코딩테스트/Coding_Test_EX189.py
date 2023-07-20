def repeat(array, ak, g):
    for k in range(g):
        array.append(ak)
    return array

def remove(array, g):
    for k in range(g):
        array.pop()
    return array

def solution(arr, flag):
    X = []
    for i in range(len(flag)):
        if flag[i] == True:
            X = repeat(X, arr[i], arr[i]*2)
        else:
            X = remove(X, arr[i])
    return X