def solution(n):
    arr1 = []
    arr2 = []
    k = str(n)
    for i in k:
        arr1.append(i)
    for i in range(len(arr1)-1, -1, -1):
        arr2.append(int(arr1[i]))
    return arr2

print(solution(12345))

"""
문제 설명
자연수 n을 뒤집어 각 자리 숫자를 원소로 가지는 배열 형태로 리턴해주세요. 예를들어 n이 12345이면 [5,4,3,2,1]을 리턴합니다.

제한 조건
n은 10,000,000,000이하인 자연수입니다.
"""
