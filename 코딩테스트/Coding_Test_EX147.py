def solution(myString, pat):
    newstr1 = myString.upper()
    newstr2 = pat.upper()

    if newstr2 in newstr1:
        return 1
    else:
        return 0
    
print(solution("AbCdEfG", "aBc"))