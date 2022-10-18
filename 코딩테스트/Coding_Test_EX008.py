def solution(x):
    num_1 = str(x)
    num_2 = int(x)
    sum_1 = 0
    arr_1 = []
    for i in range(len(num_1)):
        arr_1.append(num_1[i])
    for i in arr_1:
        sum_1 += int(i)
    if(num_2 % sum_1) == 0:
        return True
    else:
        return False


print(solution(10))
print(solution(12))
print(solution(11))
print(solution(13))

"""
문제 설명
양의 정수 x가 하샤드 수이려면 x의 자릿수의 합으로 x가 나누어져야 합니다. 예를 들어 18의 자릿수 합은 1+8=9이고, 18은 9로 나누어 떨어지므로 18은 하샤드 수입니다. 자연수 x를 입력받아 x가 하샤드 수인지 아닌지 검사하는 함수, solution을 완성해주세요.

제한 조건
x는 1 이상, 10000 이하인 정수입니다.
"""
