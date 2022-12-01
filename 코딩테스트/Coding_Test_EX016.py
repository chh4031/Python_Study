def solution(phone_number):
    arr1 = []
    answer = ""
    k = 0
    numcount = len(phone_number)-1

    while(numcount>-1):
        if(k > 3):
            arr1.append("*")
        else:
            arr1.append(phone_number[numcount])

        numcount -= 1
        k += 1
    arr1.reverse()

    for i in arr1:
        answer += i
    
    return answer

print(solution("01099998888"))

"""
문제 설명
프로그래머스 모바일은 개인정보 보호를 위해 고지서를 보낼 때 고객들의 전화번호의 일부를 가립니다.
전화번호가 문자열 phone_number로 주어졌을 때, 전화번호의 뒷 4자리를 제외한 나머지 숫자를 전부 *으로 가린 문자열을 리턴하는 함수, solution을 완성해주세요.

제한 조건
phone_number는 길이 4 이상, 20이하인 문자열입니다.
입출력 예
phone_number	return
"01033334444"	"*******4444"
"027778888"	"*****8888"
"""