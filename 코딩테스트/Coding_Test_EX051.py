def solution(money):
    k = 0
    while (money >= 5500):
        money -= 5500
        k += 1
    return [k, money]
solution(15000)