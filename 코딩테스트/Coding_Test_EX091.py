import collections

def solution(bin1, bin2):
    result = int(bin1, 2) + int(bin2, 2)
    answer = [i for i in bin(result)]
    queue = collections.deque(answer)
    queue.popleft()
    queue.popleft()
    list(queue)
    myString = ''.join(queue)
    return myString

solution("10", "11")