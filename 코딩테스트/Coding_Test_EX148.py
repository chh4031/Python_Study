def solution(num_list):
    newarr = num_list[len(num_list)-2:]
    resultarr = num_list[:]
    if newarr[0] >= newarr[1]:
        resultarr.append(newarr[1] * 2)
    else:
        resultarr.append(newarr[1] - newarr[0])
    return resultarr

print(solution([1,2,3,4,5,6,7,8,9,10]))