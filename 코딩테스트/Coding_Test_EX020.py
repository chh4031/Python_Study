# 1 2 3 [True, False, False] 1 -2 -3 = -4
def solution(absolutes, signs):
    copy_arr = absolutes[:]
    arr_sum = 0
    for i in range(0, len(copy_arr)):
        if signs[i] == False:
            k = copy_arr[i] * -1
        else:
            k = copy_arr[i] * 1
        arr_sum += k
    return arr_sum

solution([1, 2, 3], [True, False, False])