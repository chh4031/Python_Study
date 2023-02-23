def solution(num, k):
    result = []
    answer = str(num)
    g = 1
    for i in answer:
        if i == str(k):
            return g
        else:
            g += 1
    return -1
    
print(solution(29183,1))