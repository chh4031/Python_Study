def solution(num):
    num.sort()
    p = []
    m = []
    result1 = 0
    result2 = 0
    if len(num) == 2:
        return num[0] * num[1]
    else:
        for i in num:
            if i > 0:
                p.append(i)
            elif i < 0:
                m.append(i)
        try:
            result1 = p.pop() * p.pop()
        except:
            result1 = 0
        try:
            result2 = m.pop() * m.pop()
        except:
            result2 = 0
        if result1 > result2:
            return result1
        else:
            return result2
        

        
solution([10, 20, 30, 5, 5, -20, -5])