a = 1
b = 1
c = 1
mystring = ""
result = []
count = 0

for i in range(1, 1000):
    a = i
    b = a * 2
    c = a * 3
    mystring = str(a) + str(b) + str(c)
    for k in range(1, 10):
        if mystring.count(str(k)) == 1:
            count+=1
    if count == 9:
        result.append([a, b, c])
    count = 0
    if c > 1000:
        break
print(result)

