def solution(i, j, k):
    count = 0
    for g in range(i, j+1, 1):
        Str = str(g)
        myList = [a for a in Str]
        for b in myList:
            if str(b) == str(k):
                count += 1
    return count
solution(1, 13, 1)