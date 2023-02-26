def solution(before, after):
    bArray = [i for i in before]
    aArray = [i for i in after]

    bArray.sort()
    aArray.sort()

    count = 0

    for i in range(len(bArray)):
        if bArray[i] == aArray[i]:
            count += 1
    if count == len(bArray):
        return 1
    else:
        return 0
solution("olleh", "hello")