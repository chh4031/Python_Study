import time
startTime = time.time()

def factorial_iterative(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

endTime = time.time()

print('반복구현', factorial_iterative(5), endTime - startTime)