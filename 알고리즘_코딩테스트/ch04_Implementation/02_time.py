h = int(input())

count = 0
for i in range(h + 1):
    for j in range(60):
        for k in range(60):
            if '3' in str(i) + str(j) + str(k):
                count += 1
print(count)

# 각 식의 조건이 3개씩 해서 00 00 00에서 부터 N6060까지 알아봐야 하므로 각 자리에서 3이 나오는 경우만 체크하면 된다.
# 완전탐색 문제 유형