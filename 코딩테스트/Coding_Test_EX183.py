def solution(intStrs, k, s, l):
    reuslt = []
    for i in intStrs:
        if int(i[s:s+l]) > k:
            reuslt.append(int(i[s:s+l]))
    return reuslt

print(solution(["0123456789","9876543210","9999999999999"], 50000, 5, 5))