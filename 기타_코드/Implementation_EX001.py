def solution(sizes):
    k,g = 0,0
    for i in sizes:
        i.sort()
    print(sizes)
    for i in sizes:
        if i[0] > k:
            k = i[0]
        if i[1] > g:
            g = i[1]
    return k * g

solution([[3, 15], [7, 8], [16, 17], [18, 16]])