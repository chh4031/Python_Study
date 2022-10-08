import re #re 모듈 가져오기
from tkinter import * #GUI 출력을 위한 tkinter 모듈 모두 가져오기
from urllib.request import urlopen #웹 크롤링을 위한 패키지
from bs4 import BeautifulSoup #웹 크롤링을 위한 패키지

def change():
    get_txt1 = str(txt1.get("1.0", END))
    html = urlopen(get_txt1)
    bsObject = BeautifulSoup(html, "html.parser")

    str_1 = str(bsObject.head.find("title"))
    print(type(str_1))
    new_str_1 = re.sub("<title>|</title>|- YouTube", "",str_1)
    print(new_str_1)
    
    lb1.config(text = new_str_1)

root = Tk()
root.title("노래 제목 표시기")
root.geometry("320x200+0+0")
root.resizable(True, False)


txt1 = Text(root, width=30, height=1)
txt1.grid(row=1, column=1)
#txt1.pack()

btn1 = Button(root, text="확인", command=change)
btn1.grid(row=1, column=2)
#btn1.pack()

blank_1 = Label(root, text="", width=5)
blank_1.grid(row=2, column=1)
#blank_1.pack()

lb1 = Label(root, text = "Hi~", fg="blue", font=(18))
lb1.grid(row=5,column=1)
#lb1.pack()

root.mainloop()

"""
input_url = input('웹 페이지 링크 입력 : ')
html = urlopen(input_url)
bsObject = BeautifulSoup(html, "html.parser")

str_1 = str(bsObject.head.find("title"))
print(type(str_1))
new_str_1 = re.sub("<title>|</title>|- YouTube", "",str_1)
print(new_str_1)
"""

"""
목표는 웹 사이트를 자동으로 받아와서 출력을 해줘야 하는데 아직까진 수동 형태임.
직접 주소를 받아 넣으면 노래 제목을 표시해 주는 형태
유튜브 웹 사이트의 title 태그값이 다행히 유튜브 컨텐츠 제목값으로 되어져 있음을 알 수 있음.
아직 까진 프로토타입 형태로 만든것임.

참고 사이트 :
https://webnautes.tistory.com/779
https://futurum.tistory.com/353
https://docs.python.org/ko/dev/howto/urllib2.html
https://power-of-optimism.tistory.com/22
https://m.blog.naver.com/PostView.naver?blogId=amethyst_lee&logNo=222013520411&targetKeyword=&targetRecommendationCode=1
https://camplee.tistory.com/32
https://appia.tistory.com/103
https://dojang.io/mod/page/view.php?id=2441
https://scribblinganything.tistory.com/293

실행 파일을 만들기 위해서 참고한 사이트 pyinstaller를 사용함.
https://computer-science-student.tistory.com/218
"""
