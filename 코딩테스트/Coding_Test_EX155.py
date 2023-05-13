def solution(my_string, is_suffix):
    newarr = [i for i in my_string]
    findarr = [i for i in is_suffix]
    newarr.reverse()
    findarr.reverse()
    result = "".join(newarr)
    findthis = "".join(findarr)
    if result.find(findthis) == 0:
        return 1
    else:
        return 0
    
print(solution("banana", "ana"))