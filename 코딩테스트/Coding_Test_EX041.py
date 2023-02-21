def solution(array, height):
    k = 0
    for i in array:
        if i > height:
            k += 1
    return k
solution([180, 172, 175, 130], 150)