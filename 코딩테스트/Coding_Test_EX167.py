def solution(my_strings, parts):
    result = ""
    for i in range(0, len(my_strings)):
        result += (my_strings[i])[parts[i][0]:parts[i][1]+1]
    return result
        

print(solution(["progressive", "hamburger", "hammer", "ahocorasick"], [[0, 4], [1, 2], [3, 5], [7, 7]]))