def solution(my_string):
    result = my_string.split(" ")
    real = []
    for i in result:
        if i != "":
            real.append(i)
        else:
            pass
    return real

print(solution(" i    love  you"))