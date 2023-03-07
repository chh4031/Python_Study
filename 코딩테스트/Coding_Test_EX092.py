def solution(n):
    result = []
    rel = []
    for i in range(1, n):
        if n % i == 0:
            result.append(i)
            result.append(n // i)
    answer = list(set(result))
    answer.sort()
    if len(answer) != 2:
        del answer[0]

    for k in answer:
        count = 0
        for g in range(1, k+1):
            if k % g == 0:
                count += 1
        if count == 2:
            rel.append(k)
    return rel
                
solution(120)

# 예전에 소수 구하는 문제에서 봤던 내용을 바탕으로 재구성하면 풀 수 있음.