import collections as co

def solution(arr, k):
    result = []
    array = []
    for i in arr:
        if i not in result:
            result.append(i)
    a = co.deque(result)
    for i in range(k):
        try:
            array.append(a.popleft())
        except:
            array.append(-1)
    return array
    
print(solution([0, 2, 6, 4, 2], 4))