import pyautogui
import mss
import requests
import numpy
import easyocr
import cv2
import sys
import time

reader = easyocr.Reader(["en", "es"])
mon = {'top': 370, 'left': 629, 'width': 600, 'height': 150}


def createsentence():
    with mss.mss() as sct:
        mon2 = {'top': 500, 'left': 854, 'width': 300, 'height': 500}
        while True:
            url = "https://api.mymemory.translated.net/get?q="
            sep = ''
            sepspace = ' '
            im = numpy.asarray(sct.grab(mon))
            sentence = reader.readtext(im, detail=0)
            print(sentence)
            stringsentence = sep.join(sentence)
            print(stringsentence)
            im2 = numpy.asarray(sct.grab(mon2))
            options = reader.readtext(im2, detail=0)
            print(options)
            stringoptions = sepspace.join(options)
            print(stringoptions)

            for option in options:
                fullsentence = ''
                fullsentence += stringsentence
                fullsentence += ' '
                fullsentence += option
                print(fullsentence)


            # texttotranslate = sep.join(readerresult)


def fillintheblanksmethod():
    with mss.mss() as sct:
        while True:
            url = "https://api.mymemory.translated.net/get?q="
            sep = ''
            im = numpy.asarray(sct.grab(mon))
            sentence = reader.readtext(im, detail=0)
            # print(sentence)
            createsentence()

            # texttotranslate = sep.join(readerresult)
