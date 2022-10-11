def solution(arr):
    answer = 0
    for i in arr:
        answer += i
    return answer/len(arr)

k1 = [1,2,3,4]
k2 = [5,5]
b1 = solution(k1)
b2 = solution(k2)
print(b1)
print(b2)
