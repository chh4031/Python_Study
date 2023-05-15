def solution(todo_list, finished):
    result = []
    for i in range(len(todo_list)):
        if finished[i] == False:
            result.append(todo_list[i])
        else:
            pass
    return result

print(solution(["problemsolving", "practiceguitar", "swim", "studygraph"],[True, False, True, False]))