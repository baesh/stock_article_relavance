import nltk #텍스트 파일로 저장된 한국어 뉴스를 영어로 번역하여 저장.
from googletrans import Translator
from nltk.corpus import stopwords
from nltk import FreqDist
import numpy as np
import re

translator = Translator()

date = 20220425
year = 2022
month = 4
day = 25

news_text_list = []
news_amount = 30

for article_no in range(news_amount): #한 번에 너무 많은 텍스트를 번역하게 시키면, 공격을 시도하는 줄 알고 못하게 차단함. 따라서 적정 양의 텍스트를 날짜 변수를 바꿔가며 여러 번 프로그램을 실행시켜 번역.
    read_file_url = "news\\" + str(date) + ".txt"
    f = open(read_file_url, 'r', encoding='UTF8')
    article = []
    while True:
        line = f.readline()
        if not line: break
        line = line.strip('\n')
        if line != '':
            article.append(line)
    print(article)
    translated_article = []
    for i in article:
        trans = translator.translate(i, src = 'ko', dest = 'en') #뉴스 번역.
        translated_article.append(trans.text)
    f.close()

    write_file_url = "news_to_en\\" + str(date) + ".txt" #번역한 뉴스를 텍스트 파일로 저장.
    f = open(write_file_url, 'w', encoding = 'UTF8')
    for i in translated_article:
        f.write(i + '\n')
    f.close()

    if month == 1 and day == 31: #현재 날짜의 다음 날의 날짜를 계산해 주는 if문.
        month = 2
        day = 1
    elif month == 2 and day == 28 and year != (2020 or 2016 or 2012 or 2008 or 2004):
        month = 3
        day = 1
    elif month == 2 and day == 29 and year == (2020 or 2016 or 2012 or 2008 or 2004):
        month = 3
        day = 1
    elif month == 3 and day == 31:
        month = 4
        day = 1
    elif month == 4 and day == 30:
        month = 5
        day = 1
    elif month == 5 and day == 31:
        month = 6
        day = 1
    elif month == 6 and day == 30:
        month = 7
        day = 1
    elif month == 7 and day == 31:
        month = 8
        day = 1
    elif month == 8 and day == 31:
        month = 9
        day = 1
    elif month == 9 and day == 30:
        month = 10
        day = 1
    elif month == 10 and day == 31:
        month = 11
        day = 1
    elif month == 11 and day == 30:
        month = 12
        day = 1
    elif month == 12 and day == 31:
        month = 1
        day = 1
        year = year + 1
    else:
        day = day + 1

    date = year * 10000 + month * 100 + day

