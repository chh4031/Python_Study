#L1 = {anbn : n >= 0}
def anbn(n):
    if n < 0:
        print("n >= 0 but now n < 0 error")
        return
    if n == 0:
        print("", end='')
        return
    print("a", end = '')
    anbn(n - 1)
    print("b", end = '')

print("n = 0 is ", end='')
anbn(0)
print()

print("n = 1 is ", end='')
anbn(1)
print()

print("n = 2 is ", end='')
anbn(2)
print()

print("n = 3 is ", end='')
anbn(3)
print()

# 중간에 들어가는 경우가 존재해서 재귀로 돌림.
