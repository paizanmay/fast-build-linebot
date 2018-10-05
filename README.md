# fast-build-linebot
這是可以讓你快速 build 並 deploy 到 heroku 的一個 Line Chatbot 的 repo，只要跟著下面的步驟做，一下就可以完成了

# From Start
首先你要去 Line 申請一個 developer message api 帳號，記得要把 `Auto-reply messages` 設定成 Disabled，以及把 `Use webhooks` 設定成 Enabled

# How to Install
參考 [Heroku網站](https://devcenter.heroku.com/articles/getting-started-with-python)的教學
首先要完成下面4件事
* 申請 heroku 帳號並安裝 heroku CLI (`brew install heroku/brew/heroku`)
* 在本機端有安裝好 Python3
* 安裝 pipenv (```pip install pipenv```)
* 安裝 Postgres
  
接著按照下面的步驟  
首先先將這個 repo clone 回來
```bash
git clone https://github.com/paizanmay/fast-build-linebot
cd fast-build-linebot
```
接著設定 heroku
```bash
heroku login
heroku create
```
然後安裝 python packages
```bash
pipenv install
```
接著就可以對程式碼做改動了！ 
先把 `flask_test.py` 裡的兩個 Line 需要的 Token 換成 Line console 裡的你自己的 Token
改動完之後就要來 deploy 到 heroku 上了
```bash
git add .
git commit -m "Commit Message"
git push heroku master
heroku ps:scale web=1
heroku open
```
到這一步應該會打開一個網頁，網頁顯示 `Server is Running` 就沒有問題了！  
最後一步就是把 open 的網頁上的網址加上 `/callback` 回填到 Line console 的 Webhook Url 裡  
應該會是長這樣 `https://{HEROKU-APP-NAME}.herokuapp.com/callback`
如果要看 server logs 的話，執行 `heroku logs --tail` 即可 

# How to Update Code
之後對程式碼做改動後要部署到 heroku，只需要執行以下程式碼即可
```bash
git add .
git commit -m "Commit Message"
git push heroku master
```
