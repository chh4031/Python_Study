def solution(s):
    if (len(s) == 4) or (len(s) == 6):
        return s.isdigit()
    else:
        return False

solution("1234")