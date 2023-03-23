def solution(id_pw, db):
    result = ""
    for i in db:
        if i[0] == id_pw[0] and i[1] == id_pw[1]:
            result = "login"
            return result
        elif i[0] == id_pw[0]:
            result = "wrong pw"
            if result != "login":
                return result
        else:
            result = "fail"
    return result

print(solution(["meosseugi", "1234"], [["rardss", "123"], ["yyoom", "1234"], ["meosseugi", "1234"]]))