def solution(arr):
    answer = 0
    for i in arr:
        answer += i
    return answer/len(arr)

k1 = [1,2,3,4]
k2 = [5,5]
b1 = solution(k1)
b2 = solution(k2)
print(b1)
print(b2)

"""
문제 설명
정수를 담고 있는 배열 arr의 평균값을 return하는 함수, solution을 완성해보세요.

제한사항
arr은 길이 1 이상, 100 이하인 배열입니다.
arr의 원소는 -10,000 이상 10,000 이하인 정수입니다.
"""
