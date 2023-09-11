import requests #날짜별 sk 주식의 주가, 거래량을 가져와 텍스트 파일로 저장.
from bs4 import BeautifulSoup
import re

for i in range(25): #반복문 횟수는 따로 계산하지 않고, 임의로 큰 숫자를 여러번 반복함. 한번에 너무 많은 반복문을 돌리면 중간에 오류가 났을 때의 리스크가 너무 커져, 적당히 큰 숫자로 설정.
    url = 'https://finance.naver.com/item/sise_day.naver?code=034730&page='+str(i+1)
    response = requests.get(url, headers={'User-agent': 'Mozilla/5.0'})

    if response.status_code == 200:  #오류가 나면 바로 확인할 수 있게 if문으로 처리
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')
        date_li = soup.find_all(class_="tah p10 gray03") #class가 tah p10 gray03인 것만 찾아 날짜를 가져옴.
        info_li = soup.find_all(class_='num') #class가 num인 것만 찾아와 주가, 거래량을 가져옴.


        count = 0
        for i in date_li: #긁어온 데이터 형식에 맞게 정리 및, 텍스트 저장
            date = i.get_text()
            date = date.replace(".","")
            print(date)
            stock = info_li[count * 6].get_text()
            stock = stock.replace(",", "")
            print(stock)
            trading_volume = info_li[count * 6+5].get_text()
            trading_volume = trading_volume.replace(",","")
            print(trading_volume)
            file_url = "\\stock_tradingvolume\\" + str(date) + ".txt" #긁어온 뉴스를 텍스트 파일로 날짜별 저장.
            f = open(file_url, 'w', encoding="UTF8")
            f.write(stock + ' ' + trading_volume)
            f.close()
            count = count + 1
    else:
        print(response.status_code)
