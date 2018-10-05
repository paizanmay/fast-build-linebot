# fast-build-linebot
這是可以讓你快速 build 並 deploy 到 heroku 的一個 Line Chatbot 的 repo，只要跟著下面的步驟做，一下就可以完成了

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

