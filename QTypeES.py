import pyautogui
import mss
import requests
import numpy
import easyocr
import time

checkbutton = 1340, 1131
typelocation = 668, 600
mon = {'left': 752, 'top': 403, 'width': 900, 'height': 150}
reader = easyocr.Reader(['en'])

def typeinspanish():
    with mss.mss() as sct:
        while True:
            url = "https://api.mymemory.translated.net/get?q="
            sep = ' '
            im = numpy.asarray(sct.grab(mon))
            readerresult = reader.readtext(im, detail=0)
            texttotranslate = sep.join(readerresult)

            url += texttotranslate
            url += "&langpair=en|es"

            response = requests.get(url)
            response_json = response.json()

            translatedtext = response_json['responseData']['translatedText']
            print(readerresult)
            print(url)
            print(translatedtext)

            pyautogui.moveTo(typelocation, duration=1)
            pyautogui.leftClick()
            pyautogui.write(translatedtext, interval=0.1)
            pyautogui.moveTo(checkbutton, duration=1)
            pyautogui.leftClick()
            pyautogui.leftClick()

            time.sleep(0.2)
            from main import mainscript
            mainscript()
