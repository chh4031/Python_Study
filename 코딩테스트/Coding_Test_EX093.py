def solution(n, k):
    if len(n) % 2 != 0:
        ar1 = n[0::2]
        ar2 = n[1::2]
        newArray = ar1 + ar2
        return newArray[k % len(newArray)-1]
    else:
        newArray = n[0::2]
        return newArray[k % len(newArray)-1]

print(solution([1, 2, 3, 4], 3))
# 배열의 슬라이싱으로 규칙을 찾아서 이를 풀면 기존의 규칙 찾는 과정을 줄여서 런타임 에러가 나지 않음