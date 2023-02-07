def solution(price, money, count):
    newPrice = price
    total = 0
    for i in range(1, count+1):
        k = newPrice*i
        total += k
    total = total - money
    if total < 0:
        total = 0
    return total
    

solution(3, 20, 4)