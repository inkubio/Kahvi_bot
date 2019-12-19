'''
Created on 22.2.2019

@author: Antti
'''
from telegram.ext import Updater, CommandHandler
import logging
from cv2 import VideoCapture
from PIL import Image
from io import BytesIO

'''
Bot for taking pictures of the coffee machine at Inkubio guildroom and sending them to tg.
'''

'''
#Code for disasters
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.DEBUG)
'''

def kahvi_stalk(bot, update):
    '''
    Function takes image and sends image to tg after command kahvi
    '''
    camera = VideoCapture(0)
    return_value, image = camera.read()
    camera.release()
    
    image = Image.fromarray(image)  
    overlay = Image.open("cgi.png")
    overlay = overlay.resize((overlay.width // 2, overlay.height // 2))
    offset = 20
    image.paste(overlay, (offset, image.height - overlay.height - offset), overlay)


    chat_id = update.message.chat_id
    bio = BytesIO()
    bio.name = 'image.jpeg'
    image = image.save(bio,'JPEG')
    bio.seek(0)
    bot.send_photo(chat_id, photo=bio)
    
    
def start(bot, update):
    '''
    Function sends str to tg after command start
    '''

    chat_id = update.message.chat_id
    bot.send_message(chat_id=chat_id, text="Kerron sinulle, onko kiltahuoneella kahvia")
    
def main():
    updater = Updater(token='740252702:AAEcvr-_BkdW3--N5pLRTUnwBoQ81Xvtabo')
    dispatcher = updater.dispatcher
    
    start_handler = CommandHandler('start', start)
    stalk_handler = CommandHandler('kahvi', kahvi_stalk)
    dispatcher.add_handler(start_handler)
    dispatcher.add_handler(stalk_handler)

    updater.start_polling()
    updater.idle()
main()
