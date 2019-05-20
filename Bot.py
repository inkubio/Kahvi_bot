'''
Created on 22.2.2019

@author: Antti
'''
from telegram.ext import Updater, CommandHandler
import logging
from cv2 import VideoCapture, imwrite
from PIL import Image
from io import BytesIO
'''
Bot is for taking pictures of the coffee machine at Inkubio guildroom and sending them to tg.
'''

'''
#Code for disasters
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)
'''

def kahvi_stalk(bot, update):
    '''
    Function takes image and sends image to tg after command kahvi
    '''
    camera = VideoCapture(0)
    return_value, image = camera.read()
    imwrite('opencv'+str("spagu")+'.png', image)
    camera.release()

    image = Image.open('opencvspagu.png')
   
    chat_id = update.message.chat_id
    
    bio = BytesIO()
    bio.name = 'opencvspagu.png'
    image.save(bio, 'PNG')
    bio.seek(0)
    bot.send_photo(chat_id, photo=bio)
    
    
def start(bot, update):
    '''
    Function sends str to tg after command start
    '''

    chat_id = update.message.chat_id
    bot.send_message(chat_id=chat_id, text="Kerron sinulle, onko kiltahuoneella kahvia")
    
def main():
    updater = Updater(token='Token')
    dispatcher = updater.dispatcher
    
    start_handler = CommandHandler('start', start)
    stalk_handler = CommandHandler('kahvi', kahvi_stalk)
    dispatcher.add_handler(start_handler)
    dispatcher.add_handler(stalk_handler)

    updater.start_polling()
    updater.idle()
main()