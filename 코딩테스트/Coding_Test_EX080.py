def solution(numbers, target):

    def dfs(index, sum, mynum):
        # 필요한 것 2가지임. 수행동작과 종료조건
        # 종료조건 - 수행하기전에 재귀함수 처음 진입시 종료조건이 필요함.
        if index == len(myNumbers):
            if sum == mynum:
                nonlocal result
                # result는 dfs 함수에서 봤을때 비지역 변수라서 함수안의 함수에서 윗 함수에 값 변경을 위해 사용
                # 단 이를 쓰지 않으면 윗 함수의 정의된 값 그대로를 사용한다.
                # 반대로 global은 함수에서 메인코드에서의 변수에 사용
                result += 1
            return

        # 수행동작
        dfs(index + 1, sum + myNumbers[index], mynum)
        # 이거 재귀함수 다 맨 깊이 까지 들어가고 나서 해당 값이 리턴되는 순간 그 전의 연산으로 되돌아가서 아래 dfs 함수를 실행함.
        dfs(index + 1, sum - myNumbers[index], mynum)


    myNumbers = numbers
    result = 0
    dfs(0, 0, target)
    # 우리는 0번 째 인덱스부터 하나씩 탐색해갈거임.
    # 두번째 파라미터 0은 합계임. 지금까지의 합계
    print(result)

solution([4, 1, 2, 1], 4)