n = 1260 # 거스름돈
count = 0

coin_change = [500, 100, 50, 10] #큰 단위로 화폐 분류

for coin in coin_change:
    count += n // coin # 각 화폐로 거슬러줄 수 있는 동전의 갯수 세기
    n %= coin
print(count)

# 동전의 갯수가 k 일때 시간복잡도는 O(k)
# 각 동전이 배수 관계 이므로 그리디 알고리즘으로 푸는 것이 가능하다.