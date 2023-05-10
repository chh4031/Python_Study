def solution(my_string, index_list):
    result = ""
    for i in index_list:
        result += my_string[i]
    return result

print(solution("cvsgiorszzzmrpaqpe", [16, 6, 5, 3, 12, 14, 11, 11, 17, 12, 7]))