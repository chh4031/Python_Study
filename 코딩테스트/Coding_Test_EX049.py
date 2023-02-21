def solution(s1, s2):
    k = 0
    for i in s1:
        if s2.count(i) != 0:
            k += 1
    return k
solution(["a", "b", "c"], ["com", "b", "d", "p", "c"])