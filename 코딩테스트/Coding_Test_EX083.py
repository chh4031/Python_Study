def solution(n):
    global result
    result = 1
    num1 = 1
    num2 = 0
    total = n
    def dfs(num1, result):
        result *= num1
        if result == total:
            return num1
        elif result > total:
            return num1 - 1
        else:
            return dfs(num1 + 1, result)
    return dfs(num1, result)

print(solution(120))

# 재귀함수로 이용해서 해당 문제 해결
"""
재귀함수에서 return값을 제대로 설정하지 못할 경우 깊이 탐색으로 인해
이전의 return 값이 덮씌워지는 경우가 발생하여 해결에 오류가 발생할 수 있음
"""