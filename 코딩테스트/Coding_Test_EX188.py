def solution(board, k):
    result = 0
    for i in range(len(board)):
        for g in range(len(board[i])):
            if i + g <= k:
                result += board[i][g]
    return result

print(solution([[0, 1, 2],[1, 2, 3],[2, 3, 4],[3, 4, 5]], 2))