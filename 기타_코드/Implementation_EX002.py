def solution(arr):
    per1 = [1,2,3,4,5]
    per2 = [2,1,2,3,2,4,2,5]
    per3 = [3,3,1,1,2,2,4,4,5,5]

    score = {1 : 0, 2 : 0, 3 : 0}
    k = 0

    per1 *= (len(arr) // len(per1)) + 1
    per2 *= (len(arr) // len(per2)) + 1
    per3 *= (len(arr) // len(per3)) + 1

    for i in arr:
        if per1[k] == i:
            score[1] += 1
        if per2[k] == i:
            score[2] += 1
        if per3[k] == i:
            score[3] += 1
        k += 1
    result = [key for key, val in score.items() if max(score.values()) == val]
    print(score)
    return result


solution([5,4,5,5,1])