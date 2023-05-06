def solution(board, moves):
    new_list = [0]
    k = 0
    g = 1
    result = 0

    for i in moves:
        for j in board:
            if j[i-1] != 0:
                new_list.append(j[i-1])
                if new_list[k] == new_list[g]:
                    new_list.pop()
                    new_list.pop()
                    result += 2
                    k -= 1
                    g -= 1
                else:
                    k += 1
                    g += 1
                j[i-1] = 0
                break
        print(k, g)
        print(result)
    print(new_list)

solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]],[1,5,3,5,1,2,1,4])
# 답은 4가 나와야함.