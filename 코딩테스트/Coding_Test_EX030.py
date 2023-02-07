def solution(common):
    ary = common[:]
    lastNum = ary[len(ary)-1]
    if ((ary[2] + ary[0]) / 2) == ary[1]:
        return lastNum + (ary[2]-ary[1])
    else:
        return lastNum * (ary[2]/ary[1])


print(solution([1,2,4,8,16]))
print(solution([1,2,3,4]))
print(solution([-2, -4, -8]))
print(solution([-1,0,1,2]))
print(solution([4, 16, 64]))