stack = []

stack.append(5)
stack.append(4)
stack.append(3)
stack.append(2)
stack.pop()
stack.append(1)
stack.append(0)
stack.pop()

print(stack)
print(stack[::-1])
# 0에서 부터 -1씩 증가하는 슬라이싱 방식
# -1이 원소의 마지막이므로 뒤에서 부터 출력하는 결과가 만들어짐.
