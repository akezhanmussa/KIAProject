from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import pathlib


def start(update, callback):
    bot = callback.bot
    chat_id = update.message.chat_id
    bot.send_message(chat_id=chat_id, text="Hi")
    bot.send_message(chat_id=chat_id, text="Send please your photo")


def echo(update, callback):
    bot = callback.bot
    chat_id = update.message.chat_id
    image = update.message.photo[-1]

    faces_dir = 'faces'

    if not pathlib.Path(faces_dir).exists():
        pathlib.Path(faces_dir).mkdir()

    path = f'{faces_dir}/{chat_id}.jpg'
    newFile = bot.getFile(image.file_id)
    newFile.download(path)
    bot.send_message(chat_id=chat_id, text="Thanks, received")


def main():
    updater = Updater('1515946405:AAE96PUEIZr24Rnn_y-0RxYctO9acO2ukFw')
    dp = updater.dispatcher

    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(MessageHandler(Filters.all, echo))

    updater.start_polling()
    updater.idle()

    
if __name__ == '__main__':
    main()
