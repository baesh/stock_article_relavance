import requests         #네이버에서 sk관련 뉴스를 긁어오는 기능, 메모장에 긁어온 뉴스를 날짜별로 저장한다.
from bs4 import BeautifulSoup
import re

for i in range(411):    #반복문 횟수는 따로 계산하지 않고, 임의로 큰 숫자를 여러번 반복함. 한번에 너무 많은 반복문을 돌리면 중간에 오류가 났을 때의 리스크가 너무 커져, 적당히 큰 숫자로 설정.
    url = 'https://finance.naver.com/item/news_news.naver?code=034730&page='+str(i+1)+'&sm=title_entity_id.basic&clusterId='

    response = requests.get(url)

    if response.status_code == 200: #오류가 나면 바로 확인할 수 있게 if문으로 처리
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')
        date_li = soup.find_all(class_='date')  #class가 date인 것만 찾아 날짜를 가져옴.
        title_li = soup.find_all(class_='title') #class가 title인 것만 찾아와 뉴스 제목을 가져옴.
        count = 0
        for i in date_li:   #긁어온 데이터 형식에 맞게 정리 및, 텍스트 저장
            date = i.get_text()
            date = date.replace('.','')
            date = date.replace(" ", "")
            date = date[0:8]
            print(date)
            file_url = 'news\\' + str(date) + ".txt"    #긁어온 뉴스를 텍스트 파일로 날짜별 저장.
            f = open(file_url, 'a+', encoding="UTF8")
            title = title_li[count].get_text()
            print(title)
            f.write(title)
            f.close()
            count = count + 1
    else:
        print(response.status_code)
