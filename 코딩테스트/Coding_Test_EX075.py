def solution(order):
    count = 0
    result = str(order)
    for i in result:
        if i == "3" or i == "6" or i == "9":
            count += 1
    return count
solution(29423)