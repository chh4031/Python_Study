def recursive_funtion(i):
    if i == 3:
        return
    print(i , "에서 ", i + 1, "번재 재귀함수 실행")
    recursive_funtion(i + 1)
    print(i, "번재 재귀 함수 종료")
recursive_funtion(1)

# 재귀함수의 실행이후 리턴하면서 이전에 실행되지 못한 값이 스택형식으로 구현됨.