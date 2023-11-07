# stock_article_relavance
Finding relavance of stock and article
<br>
#Task

Given article title data of certain company(in this case 'SK'), find the relavance of news data and stock price(consider if the stock price will increase or decrease)..

<br>
#Idea

-Use RNN for training

-Batch size: 15

-Epoch: 5

<br>
#Word embedding

-Translate Korean article title data into English

-Change English data into stemmer

-Allocate number to stemmers by their appearance number


#Codes

-Get stock, trading volume data: sk_stock_tradingvolume.py

-Get article title data: sk_news.py

-Get translate article title to english: news_translate.py

-Change article title to numbers(embedding): news_to_index.py

-Training: news_train_1.py, news_train_2.py

<br>
#Result

![캡처](https://github.com/baesh/stock_article_relavance/assets/18441461/0d79c51b-718f-46cb-84ee-03c3764a066d)

Result of 'news_train_1.py' (regulate rate of stock increasing and decreasing data before training)

![캡처2](https://github.com/baesh/stock_article_relavance/assets/18441461/36a38fd6-616a-427a-a00e-41df67defd3b)

Result of 'news_train_1.py' (don't regulate rate of stock increasing and decreasing data before training)

<br>
Too much overfitting -> can't predict stock price only with article title data
