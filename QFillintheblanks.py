import pyautogui
import mss
import requests
import numpy
import easyocr
import cv2
import sys
import time

reader = easyocr.Reader(["en", "es"])
mon = {'left': 808, 'top': 428, 'width': 590, 'height': 150}

def fillintheblanks():
    with mss.mss() as sct:
        while True:
            url = "https://api.mymemory.translated.net/get?q="
            sep = ''
            im = numpy.asarray(sct.grab(mon))
            readerresult = reader.readtext(im, detail=0)
            texttotranslate = sep.join(readerresult)
            from main import mainscript
            mainscript()