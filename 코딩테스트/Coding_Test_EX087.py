def solution(emergency):
    peopleList = {}
    newList = [i for i in emergency]
    newList.sort(reverse=True)
    result = []
    real = []
    k = 1
    for i in newList:
        result.append([i, k])
        k += 1
    for i in emergency:
        for g in result:
            if i == g[0]:
                real.append(g[1])
    return real
solution([3, 76, 24])