def solution(mystr, n):
    result = []
    k = n
    num1 = 0
    if (len(mystr) % n) != 0:
        controll = (len(mystr) // n + 1)
    else:
        controll = (len(mystr) // n)
    for i in range(controll):
        result.append(mystr[num1:k])
        num1 += n
        k += n
        print(result)
    return result
solution("abc1Addfggg4556b", 6)