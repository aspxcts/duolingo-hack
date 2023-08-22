import pyautogui
import mss
import requests
import numpy
import easyocr
import time

checkbutton = 1340, 1131
reader = easyocr.Reader(["en", "es"])
mon = {'left': 752, 'top': 403, 'width': 590, 'height': 170}


def typeinenglish():
    with mss.mss() as sct:
        while True:
            url = "https://api.mymemory.translated.net/get?q="
            sep = ''
            im = numpy.asarray(sct.grab(mon))
            readerresult = reader.readtext(im, detail=0)
            print(readerresult)
            texttotranslate = sep.join(readerresult)

            url += texttotranslate
            url += "&langpair=es|en"

            response = requests.get(url)
            response_json = response.json()

            translatedtext = response_json['responseData']['translatedText']
            print(url)
            print(translatedtext)

            pyautogui.write(translatedtext, interval=0.1)
            pyautogui.moveTo(checkbutton, duration=1)
            pyautogui.leftClick()
            pyautogui.leftClick()

            time.sleep(0.2)
            from main import mainscript
            mainscript()
