import nltk #번역한 뉴스를 숫자로 바꾸어 저장.
from nltk.corpus import stopwords
from nltk import FreqDist
import numpy as np
import re
nltk.download('stopwords')

def article_to_stemmer(text): #뉴스를 형태소의 꼴로 분해하는 함수.
    only_english = re.sub('[^a-zA-Z]', ' ', text)
    no_capital = only_english.lower().split()
    #print(no_capital)
    stops = set(stopwords.words('english'))
    no_stops = [word for word in no_capital if not word in stops]
    #print(no_stops)
    stemmer = nltk.stem.SnowballStemmer('english')
    stemmer_words = [stemmer.stem(word) for word in no_stops]
    #print(stemmer_words)
    return stemmer_words

news_amount = 477 #총 처리할 뉴스 텍스트 파일의 수

date = 20210202 #처리를 시작할 날짜
year = 2021
month = 2
day = 2

news_text_list = []
for article_no in range(news_amount):
    file_url = "news_to_en\\" + str(date) + ".txt"
    f = open(file_url, 'r', encoding='UTF8')
    article = []
    while True:
        line = f.readline()
        if not line: break
        line = line.strip('\n')
        if line != '':
            article.append(line)
    print(article)

    article_analyze = []
    for i in article:
        analyzed = article_to_stemmer(i) #뉴스를 형태소 단위로 분해
        article_analyze.append(analyzed)

    print(article_analyze)
    news_text_list.append(sum(article_analyze,[]))

    if month == 1 and day == 31: #현재 날짜의 다음 날의 날짜 계산.
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
    f.close()

word_list = sum(news_text_list, []) #구한 형태소를 리스트에 전부 저장.
vocab = FreqDist(word_list) #각 형태소가 몇 번 나왔는지 체크하여 그 횟수를 저장
sorted_vocab = sorted(vocab.items(), reverse=True, key=lambda item: item[1])
index_dict = {}
index_no = 1
for key, value in sorted_vocab:
    print(key + ': ' + str(value))
    if value > 1 and len(key) != 1: #사용 횟수가 2회 이상, 길이가 1 초과인 형태소만을 골라와, 재배열.
        index_dict[key] = index_no
        index_no = index_no + 1

print(index_no) #3298


date = 20210202
year = 2021
month = 2
day = 2


for article_no in range(news_amount):
    file_url = "indexed_news\\" + str(date) + ".txt"
    f = open(file_url, 'w', encoding='UTF8')

    for i in news_text_list[article_no]: #각 뉴스의 형태소를 숫자로 바꾼 후, 그 숫자의 배열을 텍스트로 저장.
        if i in index_dict:
            f.write(str(index_dict[i])+'\n')

    if month == 1 and day == 31: #현재 날짜의 다음 날의 날짜 계산.
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
    f.close()
