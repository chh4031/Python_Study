# qwert = e , qwer = we

def solution(Str):
    Strb = list(Str)
    k = 0
    Sum = 0
    for i in range(1, len(Strb)+1):
        k += i
    Sum = int((k / len(Strb))-1)

    if((len(Strb)%2)==0):
        return Strb[Sum]+Strb[Sum+1]
    else:
        return Strb[Sum]

solution("qwerta")