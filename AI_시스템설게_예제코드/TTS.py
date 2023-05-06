from gtts import gTTs
from playsound import playsound
import os

news = "이상 관리사무소에서 안내드립니다."
news2 = "동해물과 백두산이 마르고 닳도록"
tts = gTTs(text=news, lang="ko")
tts2 = gTTs(text=news2, lang="ko")
tts.save("new_test.mp3")
tts2.save("news_test.mp3")
playsound("news_test.mp3", True)
playsound("news2_test.mp3", True)
os.remove("news_test.mp3")
os.remove("news2_test.mp3")

