from sklearn import datasets
from sklearn import svm

digit = datasets.load_digits()
# digit 데이터를 불러오는 것임.x
s=svm.SVC(gamma = 0.1, C = 10)
# s의 역할은 그저 빈 모델을 하나 생성하는 정도임.
s.fit(digit.data, digit.target)
# 이해를 못한 이유 : data는 피쳐(특징), target은 라벨(피쳐를 통해 나온값임.)
print(digit.data[0])
# 이걸로 나온 피쳐값 숫자 64개의 값으로 만들어진것이 아래것임.
print(digit.target[0])
# 이거는 위의 피쳐값 숫자 64개로 만들어진 숫자 0을 의미함. (이거 그려보면암)

new_d = [digit.data[0], digit.data[1], digit.data[2]]
# 그래서 각 피쳐값 3개를 넘겨줌.
result = s.predict(new_d)
# result에는 예측값을 던져주는 것임. 위의 3개의 피쳐값으로 나온 결과를 예측으로 던져줌

print("예측값 :", result)
print("참값 :", digit.target[0], digit.target[1], digit.target[2])
# 그래서 예측값(학습해서 나온거)이랑 원래 값을 비교해봄

result_2 = s.predict(digit.data)
# 이제 예측값으로 모든 피쳐값을 다 던져줌
correct = [i for i in range(len(result_2)) if result_2[i] == digit.target[i]]
accuracy = len(correct)/len(result_2)
print("정확도 : ", accuracy*100, "%")
