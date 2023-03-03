from collections import deque

def solution(num_list, n):
    de = deque(num_list)
    result = []
    answer = []
    for g in range(len(num_list)//n):
        de.append([de[i] for i in range(n)])
        for k in range(n):
            de.popleft()
        # print(de)
    return list(de)

solution([1, 2, 3, 4, 5, 6, 7, 8], 2)

# 큐로 구현
# 리스트를 for로 돌려서 생성하는 방식을 이용하면됨.
# num_list % n != 0 이면 제대로 된 배열 생성을 못하는 결과값이 도출됨.