a = str(472)
b = str(385)
c = [i for i in b]
count = str(0)
result = 0

d = []
for i in b:
    d.append(int(a)*int(i))
d.reverse()
for k in range(len(d)):
    d[k] = int(str(d[k]) + count*k)
    print(d[k])
    result += d[k]
print(result)

