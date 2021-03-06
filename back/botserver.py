from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import pathlib
import requests
import json

db = {}

def start(update, callback):
    bot = callback.bot
    chat_id = update.message.chat_id
    bot.send_message(chat_id=chat_id, text="Hi")
    bot.send_message(chat_id=chat_id, text="Send please your photo")

def echo(update, callback):
    global db
    bot = callback.bot
    chat_id = update.message.chat_id
    image = update.message.photo[-1]

    faces_dir = 'faces'

    if not pathlib.Path(faces_dir).exists():
        pathlib.Path(faces_dir).mkdir()

    if chat_id not in  db: 
        db[chat_id] = image.file_id
        with open("db.json", "w") as f:
            json.dump(db, f)

    path = f'{faces_dir}/{chat_id}.jpg'
    newFile = bot.getFile(image.file_id)
    newFile.download(path)
    bot.send_message(chat_id=chat_id, text="Thanks, received")


def main():
    global db
    path = 'db.json'

    if not pathlib.Path(path).exists():
        pathlib.Path(path).touch()

    with open("db.json") as f:
        try:
            db = json.load(f)
        except:
            db = {}

    updater = Updater('1515946405:AAE96PUEIZr24Rnn_y-0RxYctO9acO2ukFw')
    dp = updater.dispatcher

    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(MessageHandler(Filters.all, echo))

    updater.start_polling()
    updater.idle()

    
if __name__ == '__main__':
    main()
