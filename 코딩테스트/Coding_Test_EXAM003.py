from collections import deque

def cut(n):
    a1 = n.popleft()
    a2 = n.popleft()
    a3 = n.popleft()
    a4 = n.popleft()
    a5 = n.popleft()
    a6 = n.popleft()
    a7 = n.popleft()
    a8 = n.popleft()
    return a1+a2, a3+a4, a5+a6, a7+a8

def solution(serial):
    result = deque(serial)
    select = {
        "01" : "male",
        "02" : "female", 
        "10" : "operation", 
        "11" : "sales",
        "12" : "develop",
        "13" : "finance",
        "14" : "law",
        "15" : "research",
        }
    pSex, pDev, pTeam, pNum= cut(result)
    answer = 0
    for i in (pSex+pDev+pTeam):
        answer += int(i)
    valid = answer % 13
    print(pSex, pDev, pTeam, pNum)
    if valid == int(pNum):
        return (select[pSex]+"/"+select[pDev]+"/"+str(int(pTeam))+"team"+"/"+"valid")
    else:
        return (select[pSex]+"/"+select[pDev]+"/"+str(int(pTeam))+"team"+"/"+"invalid")
    
print(solution("02131003"))
