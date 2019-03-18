'''
Created on 22.2.2019

@author: Antti
'''
from telegram.ext import Updater
from telegram.ext import CommandHandler
import logging

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)


#def start(update, context):
#    context.bot.send_message(chat_id=update.message.chat_id, text="I'm a bot, please talk to me!")

def start(bot, update):
    chat_id = update.message.chat_id
    bot.send_message(chat_id=chat_id, text="En tieda onko kahvi")
    
def main():
    updater = Updater(token='740252702:AAGwf5qeXBrO4TGwjBj1aBxD5aGYqVGQyr4')
    dispatcher = updater.dispatcher
    start_handler = CommandHandler('start', start)
    dispatcher.add_handler(start_handler)
    updater.start_polling()
    updater.idle()
main()