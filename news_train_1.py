import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import urllib.request
import os
import math
from sklearn.model_selection import train_test_split
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from pandas import Series, DataFrame
from tensorflow.keras.layers import SimpleRNN, Embedding, Dense
from tensorflow.keras.models import Sequential


def prev_date_cal(date):            #날짜 넣으면 하루 전날 날짜 리턴
    day = date % 100
    month = math.floor(date / 100) % 100
    year = math.floor(date / 10000)

    if month == 1 and day == 1:
        year = year - 1
        day = 31
        month = 12
    elif month == 2 and day == 1:
        month = 1
        day = 31
    elif month == 3 and day == 1 and year == (2020 or 2016 or 2012 or 2008 or 2004):
        month = 2
        day = 29
    elif month == 3 and day == 1 and year != (2020 or 2016 or 2012 or 2008 or 2004):
        month = 2
        day = 28
    elif month == 4 and day == 1:
        month = 3
        day = 31
    elif month == 5 and day == 1:
        month = 4
        day = 30
    elif month == 6 and day == 1:
        month = 5
        day = 31
    elif month == 7 and day == 1:
        month = 6
        day = 30
    elif month == 8 and day == 1:
        month = 7
        day = 31
    elif month == 9 and day == 1:
        month = 8
        day = 31
    elif month == 10 and day == 1:
        month = 9
        day = 30
    elif month == 11 and day == 1:
        month = 10
        day = 31
    elif month == 12 and day == 1:
        month = 11
        day = 30
    else:
        day = day - 1
    prev_date = day + month * 100 + year * 10000
    return prev_date

dir_path = "stock_tradingvolume"

date_li = []
for (root, directories, files) in os.walk(dir_path):
    for file in files:
        file_name = file.strip('.txt')
        date_li.append(int(file_name))

dataset = []
for date in date_li:
    if date > 20210202:
        try:
            data = []   #날짜, 전날 주가 상승 여부(상승 1, 하락 또는 변동없음 0), 전날 뉴스

            data.append(date)

            stock_file_url = "stock_tradingvolume\\" + str(date) + ".txt"
            f = open(stock_file_url, 'r', encoding='UTF8')
            line = f.readline()
            no_li = line.split(" ")
            current_stock = int(no_li[0])
            f.close()

            prev_date = prev_date_cal(date)
            prev_stock_file_url = "stock_tradingvolume\\" + str(prev_date) + ".txt"
            f = open(prev_stock_file_url, 'r', encoding='UTF8')
            line = f.readline()
            prev_no_li = line.split(" ")
            prev_stock = int(prev_no_li[0])
            f.close()

            if((current_stock - prev_stock) > 0):
                data.append(1)
            else:
                data.append(0)

            index_file_url = "indexed_news\\" + str(prev_date) + ".txt"
            f = open(index_file_url, 'r', encoding='UTF8')
            text = []
            while True:
                line = f.readline()
                if not line: break
                line = line.strip('\n')
                if line != '':
                    text.append(int(line))
            f.close()
            data.append(text)

            dataset.append(data)
        except:
            pass


x = []
y = []
for i in dataset:
    x.append(i[2])
    y.append(i[1])

x_data = Series(x)  #sk 주식의 뉴스 데이터
y_data = Series(y) #sk 주식의 등락 데이터

x_train, x_test, y_train, y_test = train_test_split(x_data,y_data, test_size=0.2, random_state=0, stratify=y_data)  #train 0.8, test 0.2 비율로 데이터 분류, 각 데이터의 비율은 y데이터를 기준으로 맞춤.
print(x_train)
print('----------train_data_ratio----------')
print(f'stock increase: {round(y_train.value_counts()[1]/len(y_train) * 100,3)}%')
print(f'stock decrease: {round(y_train.value_counts()[0]/len(y_train) * 100,3)}%')
print('----------test_data_ratio----------')
print(f'stock increase: {round(y_test.value_counts()[1]/len(y_test) * 100,3)}%')
print(f'stock decrease: {round(y_test.value_counts()[0]/len(y_test) * 100,3)}%')

max_x_len = max(len(sample) for sample in x_train)
x_train_padded = pad_sequences(x_train, maxlen=max_x_len)
print("train data size : ", x_train_padded.shape)

embedding_dim = 20
hidden_units = 20
vocab_size = 3298

model = Sequential() #rnn을 사용하여 학습
model.add(Embedding(vocab_size, embedding_dim))
model.add(SimpleRNN(hidden_units))
model.add(Dense(1, activation='sigmoid'))

model.compile(optimizer='rmsprop', loss='binary_crossentropy', metrics=['acc'])
history = model.fit(x_train_padded, y_train, epochs=5, batch_size=15, validation_split=0.3)


x_test_padded = pad_sequences(x_test, maxlen = max_x_len)
print("\n 테스트 정확도: %.4f" % (model.evaluate(x_test_padded, y_test)[1]))

epochs = range(1, len(history.history['acc']) + 1)
plt.plot(epochs, history.history['loss'])
plt.plot(epochs, history.history['val_loss'])
plt.title('model loss')
plt.ylabel('loss')
plt.xlabel('epoch')
plt.legend(['train', 'val'], loc='upper left')
plt.show()