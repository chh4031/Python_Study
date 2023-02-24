from collections import deque
# 큐 구현을 위한 deque 라이브러리르 이용한다.
queue = deque()

queue.append(5)
queue.append(4)
queue.append(3)
queue.append(2)
queue.popleft()
queue.append(1)
queue.append(0)
queue.popleft()

print(queue)
# 들어온 순서대로
queue.reverse()
print(queue)
# 마지막에 들어온 순서대로
print(type(queue))
# 이거 리스트형 자료형 아님. deque의 객체형이므로 list()로 바꿔서 사용해야함.