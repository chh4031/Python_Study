def solution(n):
    answer = []
    for i in range(0, n+1):
        if i % 2 != 0:
            answer.append(i)
    return answer
solution(10)