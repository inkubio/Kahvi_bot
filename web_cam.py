'''
Created on 13.2.2019

@author: Antti
'''
import cv2
from PIL import Image

def main():
    camera = cv2.VideoCapture(0)
    return_value, image = camera.read()
    cv2.imwrite('opencv'+str("spagu")+'.png', image)
    camera.release()
    
    image = Image.open('opencvspagu.png')
    image.show()
main()