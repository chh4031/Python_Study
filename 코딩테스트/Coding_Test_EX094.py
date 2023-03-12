def solution(array):
    count = 0
    result = ""
    for i in array:
        result += str(i)
    for k in result:
        if k == "7":
            count += 1
    return count

solution([7, 77, 17])