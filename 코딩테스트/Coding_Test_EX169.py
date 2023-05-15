def solution(names):
    result = []
    for i in range(0, len(names), 5):
        result.append(names[i])
    return result

print(solution(["nami", "ahri", "jayce", "garen", "ivern", "vex", "jinx"]))