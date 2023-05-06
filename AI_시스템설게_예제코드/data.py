from sklearn import datasets

d=datasets.load_iris()
# print(d.DESCR)
for i in range(0, len(d.data)):
    print(i+1,d.data[i],d.target[i])
    