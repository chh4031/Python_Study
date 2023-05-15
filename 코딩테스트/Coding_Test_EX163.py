def solution(arr, delete_list):
    arr1 = arr[:]
    for i in delete_list:
        try:
            arr1.remove(i)
        except:
            pass
    return arr1

print(solution([293, 1000, 395, 678, 94], [94, 777, 104, 1000, 1, 12]))