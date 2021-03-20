from flask import Flask, request
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

app = Flask(__name__)


@app.route('/nomask', methods=['POST'])
def index():
    request_data = request.get_json()
    print(request_data)
    chat_id = request_data['id']
    bot = Updater('1515946405:AAE96PUEIZr24Rnn_y-0RxYctO9acO2ukFw').bot
    bot.send_message(chat_id=chat_id, text="You are not wearing mask 🤬")
    return "Hello World"


if __name__ == "__main__":
    app.run(debug=True)
