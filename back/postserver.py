from flask import Flask, request
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import botserver
import json
app = Flask(__name__)
bot = Updater('1515946405:AAE96PUEIZr24Rnn_y-0RxYctO9acO2ukFw').bot
admin_id = '359715487'


@app.route('/nomask', methods=['POST'])
def index():
    request_data = request.get_json()
    chat_id = request_data['id']
    location = request_data['location']

    bot.send_message(chat_id=chat_id, text="You are not wearing mask 🤬")
    bot.send_message(chat_id=chat_id, text="I know your location, shit")
    bot.send_message(chat_id=chat_id, text=location)

    return "Hello Pidor"

@app.route('/admin', methods=['POST'])
def admin():
    request_data = request.get_json()
    chat_id = request_data['id']
    location = request_data['location']

    with open("db.json") as f:
        db = json.load(f)
    image_id = db[chat_id]

    bot.send_message(chat_id=admin_id, text="This bastard does not wear mask")
    bot.send_photo(chat_id=admin_id, photo=image_id)
    bot.send_message(chat_id=admin_id, text="Its location: ")
    bot.send_message(chat_id=admin_id, text=location)
    return "Hello Pidor"

if __name__ == "__main__":
    app.run(debug=True)
