def solution(numbers, direction):
    if direction == "right":
        k = numbers.pop()
        numbers.insert(0, k)
        return numbers
    else:
        k = numbers[0]
        del numbers[0]
        numbers.append(k)
        return numbers
solution([1,2,3], "right")