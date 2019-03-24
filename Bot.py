'''
Created on 22.2.2019

@author: Antti
'''
from telegram.ext import Updater
from telegram.ext import CommandHandler
import logging
import cv2
from PIL import Image
from io import BytesIO

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)


def fuksi_stalk(bot, update):
    
    camera = cv2.VideoCapture(0)
    return_value, image = camera.read()
    cv2.imwrite('opencv'+str("spagu")+'.png', image)
    camera.release()
    
    image = Image.open('opencvspagu.png')
    '''
    image.show()
    '''
    chat_id = update.message.chat_id
    '''
    bot.send_photo(chat_id=chat_id, photo=open('spagu/laah_puuh.jpeg', 'rb'))
    '''
    bio = BytesIO()
    bio.name = 'opencvspagu.png'
    image.save(bio, 'PNG')
    bio.seek(0)
    bot.send_photo(chat_id, photo=bio)
    
def start(bot, update):
    chat_id = update.message.chat_id
    bot.send_message(chat_id=chat_id, text="En tieda onko kahvia")
    
def main():
    updater = Updater(token='Token')
    dispatcher = updater.dispatcher
    
    start_handler = CommandHandler('start', start)
    stalk_handler = CommandHandler('fuksi_stalk', fuksi_stalk)
    dispatcher.add_handler(start_handler)
    dispatcher.add_handler(stalk_handler)

    updater.start_polling()
    updater.idle()
main()