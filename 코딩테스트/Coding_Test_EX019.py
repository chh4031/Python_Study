# 리스트의 sort를 이용해서 정렬이후 가장 작은 수를 찾은 후 그 다음에 해당 값을 list.index로 찾는다.
def solution(li):
    if(len(li)>1):
        arr_copy = li
        arr_copy.remove(min(arr_copy))
        return arr_copy
    else:
        return [-1]
    

solution([7,1,2,3])