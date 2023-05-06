from sklearn.linear_model import Perceptron

x = [[0, 0], [0, 1], [1, 0], [1, 1]]
y = [-1,1,1,1]

p = Perceptron()
p.fit(x, y)

print("학습된 퍼셉트론의 매개변수: ", p.coef_, p.intercept_)
print("훈련집합에 대한 예측: ", p.predict(x))
print("정확률 측정: ", p.score(x, y)*100)
