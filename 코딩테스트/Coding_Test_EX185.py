# def solution(players, callings):
#     newPlayers = players[::]
#     for i in callings:
#         play = newPlayers.index(i)
#         newPlayers[play-1], newPlayers[play] = newPlayers[play], newPlayers[play-1]
#     return newPlayers

# print(solution(["mumu", "soe", "poe", "kai", "mine"], ["kai", "kai", "mine", "mine"]))

def solution(players, callings):
    result = []
    dic1 = {}
    dic2 = {}
    for i in range(len(players)):
        dic1[players[i]] = i
        dic2[i] = players[i]
    # print(dic1)
    # print(dic2)
    for k in callings:
        a = dic1[k]
        # print(a)
        dic1[dic2[a-1]] = a
        dic1[dic2[a]] = a-1
        dic2[a] = dic2[a-1]
        dic2[a-1] = k
    for g in range(len(players)):
        result.append(dic2[g])
    return result



print(solution(["mumu", "soe", "poe", "kai", "mine"], ["kai", "kai", "mine", "mine"]))

# {'mumu': 0, 'soe': 1, 'poe': 2, 'kai': 3, 'mine': 4}
# {0: 'mumu', 1: 'soe', 2: 'poe', 3: 'kai', 4: 'mine'}