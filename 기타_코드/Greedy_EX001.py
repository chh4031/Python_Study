def solution(n, lost, res):
    count = 0
    total = 0
    new_res = res[:]
    new_lost = lost[:]
    new_res.sort()
    new_lost.sort()

    ary_1 = []

    print("new_res = ", new_res)
    print("new_lost = ", new_lost)

    for r1 in lost: 
        for r2 in res:
            if r1 == r2:
                new_res.remove(r2)
                new_lost.remove(r1)
            print(r1, r2)
    print("new_res = ", new_res)
    print("new_lost = ", new_lost)

    for i in new_res:
        ary_1.append([i, i-1, i+1])
    print("ary_1 = ", ary_1)

    for k in new_lost:
        for g in range(len(ary_1)):
            if k in ary_1[g]:
                print("TRUE")
                count += 1
                del ary_1[g]
                break
    print("ary_1 = ", ary_1)


                
    total = (n - len(new_lost)) + count
    print(total)
        

solution(30, [1], [])
'''
test case
3 [3] [8] => count : 2
5 [2, 4] [1, 3, 5] => count : 5
12 [3, 5] [5, 7, 8] => count : 11
11 [3, 4, 5] [2, 4, 5] => count : 11
5 [2, 4] [3] => count : 4
12 [1, 2, 3, 4, 11] [1, 2, 3, 6] => count : 10
12 [1] [1] => count : 12
5 [1,2,3,4,5] [] => count : 5



조건
1. 
'''