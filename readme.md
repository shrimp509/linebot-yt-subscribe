
# 查詢 Youtube Channel 訂閱數的聊天機器人
使用 Django 框架（Python）打造，主要是裡面的爬蟲

我寫了四篇文章來介紹這個專案，
* [(番外篇-架構介紹)[不做怎麼知道系列之Android開發者的30天後端養成故事 Day23] - 來問問你認識的Youtuber的訂閱數吧~ #Django #GAE #LineChatBot](https://ithelp.ithome.com.tw/articles/10230260)
* [(番外篇-爬蟲)[不做怎麼知道系列之Android開發者的30天後端養成故事 Day24] - 來問問你認識的Youtuber的訂閱數吧~ #crawler #python #socialblade](https://ithelp.ithome.com.tw/articles/10230271)
* [(番外篇-LineBot)[不做怎麼知道系列之Android開發者的30天後端養成故事 Day25] - 來問問你認識的Youtuber的訂閱數吧 #Django #LineBotSDK #ngrok](https://ithelp.ithome.com.tw/articles/10230282)
* [(番外篇-GAE)[不做怎麼知道系列之Android開發者的30天後端養成故事 Day26] - 來問問你認識的Youtuber的訂閱數吧~ #Django #GAE #LineChatBot](https://ithelp.ithome.com.tw/articles/10230323)


# 截圖
![https://github.com/shrimp509/linebot-yt-subscribe/blob/master/screenshots/intro.jpeg](https://github.com/shrimp509/linebot-yt-subscribe/blob/master/screenshots/intro.jpeg)

# 怎麼使用？
先去 Line Developer 申請一個 provider，然後綁定 webhook url

然後再
* Step1: `$ git clone https://github.com/shrimp509/linebot-yt-subscribe.git`
* Step2: `$ pip3 install django linebot-sdk`
* Step3: `$ python3 manage.py runserver`
* Step4: 用 `ngrok` 產出 https 的 webhook url