def solution(Ary):
    aryMax = max(Ary)
    aryMin = min(Ary)
    count = 0
    for i in range(aryMax - aryMin + 1, aryMax + 1):
        count += 1
    for k in range(aryMax + 1, aryMax + aryMin):
        count += 1
    return count