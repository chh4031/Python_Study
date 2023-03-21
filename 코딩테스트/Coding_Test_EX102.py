def solution(keyinput, board):
    dxp = board[0] // 2
    dyp = board[1] // 2
    dxm = -(board[0] // 2)
    dym = -(board[1] // 2)
    print(dxp, dyp, dxm, dym)
    result = [0,0]
    for i in keyinput:
        if i == "right":
            result[0] += 1
            if result[0] > dxp:
                result[0] -= 1
                continue
        if i == "left":
            result[0] -= 1
            if result[0] < dxm:
                result[0] += 1
                continue
        if i == "up":
            result[1] += 1
            if result[1] > dyp:
                result[1] -= 1
                continue
        if i == "down":
            result[1] -= 1
            if result[1] < dym:
                result[1] += 1
                continue
    return result
        
print(solution(["right", "right", "right", "right","left", "left", "left", "left"], [5,5]))