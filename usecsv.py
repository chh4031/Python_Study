import csv, re, os

def oncsv():
    try:
        os.chdir(r'C:\Users\LAPTOP\Desktop\cho_hyeon_ho')
        print('usecsv on LAPTOP')
    except:
        os.chdir(r'C:\Users\CHOBOJJAL\Desktop\cho_hyeon_ho')
        print('usecsv on DESKTOP')
#위의 함수는 풀러오는 환경에 따라 다르게 실행될 수 있게 구성.
#작업폴더는 바탕화면으로 동일 단, 노트북이냐 데스크탑이냐에 따라 다름.

def opencsv(filename):
    f = open(filename, 'r')
    reader = csv.reader(f)
    output = []
    for i in reader:
        output.append(i)
    return output
#csv파일을 가져와서 출력하는 함수


def writecsv(filename, the_list):
    f = open(filename, 'w', newline='')
    csvob = csv.writer(f, delimiter=',')
    csvob.writerows(the_list)
    f.close()
#csv파일을 추가하는 함수

def switch(listName):
    for i in listName:
        for j in i:
            try:
                i[i.index(j)] = float(re.sub(',','',j))
            except:
                pass
    return listName
#리스트로 만든 csv파일의 내용을 ,제거 후 float로 변형하기 위한 함수
'''단 for문이 2개인 이유가 만들어진 csv의 파일리스트가 리스트안에 리스트인 2차원으로
구성되어 있기 때문이다. '''
