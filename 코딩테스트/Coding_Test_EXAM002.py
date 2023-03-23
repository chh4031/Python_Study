def solution(text, anagram, sw):
    result = [0] * len(anagram)
    answer = ""
    if sw == True:
        for i in range(len(text)):
            result[anagram[i]] = text[i]
        answer = ''.join(result)
        return answer
    else:
        for i in anagram:
            answer += text[i]
        return answer

solution("lleoH", [4, 2, 0, 1, 3], False)

"""
10번
"""