from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

app = Flask(__name__)

line_bot_api = LineBotApi("raJIOE2LaacIFk0uUKcF10plUSqcQUJdyQLryRe1X8FFs7dzhrj2vx14vWCn7t9SlGvYPrMtbxefCbQnLhsms5VJASBSr64xeRhf9ixXT3f0aFzQL6asptBQFCIMICNd3RgajKq/m0GKAE5ImXJJaAdB04t89/1O/w1cDnyilFU=Issue")
handler = WebhookHandler('cf00401a45cbd9fd2b366408f4759cb3')


@app.route("/", methods=['GET'])
def index():
    return 'Server is Running'


@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    print("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=event.message.text))


if __name__ == "__main__":
    app.run()
