import time
startTime = time.time()

def factorial_recursive(n):
    if n <= 1:
        return 1
    return n * factorial_recursive(n-1)

endTime = time.time()

print('재귀구현', factorial_recursive(5), endTime-startTime)