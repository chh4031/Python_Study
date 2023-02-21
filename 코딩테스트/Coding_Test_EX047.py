def solution(numbers):
    numbers.sort()
    return numbers[len(numbers)-1] * numbers[len(numbers)-2]

solution([1,6,2,8,11,2])