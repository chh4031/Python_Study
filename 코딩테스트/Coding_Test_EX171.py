def solution(str_list, ex):
    result = ""
    for i in str_list:
        if ex in i:
            pass
        else:
            result += i
    return result

print(solution(["abc", "def", "ghi"], "ef"))