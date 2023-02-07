# [0,1,2,3,5,6,8,9] => 4, 7 => 11 / 0~9
def solution(arr):
    k=0
    g=0
    for i in range(0,10):
        k += i
    g =  sum(arr)
    return k-g


solution([0,1,2,3,5,6,8,9])