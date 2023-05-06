from sklearn import datasets
from matplotlib import pyplot as plt

digit = datasets.load_digits()

plt.figure(figsize=(3,3))
plt.imshow(digit.images[13], cmap = plt.cm.gray_r)

plt.show()
print(digit.data[13])
print("이숫자는", digit.target[13], "입니다.")