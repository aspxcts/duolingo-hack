import pyautogui
import mss
import requests
import numpy
import easyocr
import cv2
import sys
import time
import re

reader = easyocr.Reader(["en", "es"])
mon = {'top': 267, 'left': 585, 'width': 550, 'height': 200}


def removefirstword(input_string):
    words = input_string.split()
    new_string = ' '.join(words[1:])
    return new_string


def extractword(input_string):
    pattern = r'"([^"]*)"'
    match = re.search(pattern, input_string)

    if match:
        extracted_word = match.group(1)
        return extracted_word
    else:
        return None


def extract(input_string, target_word):
    index = input_string.find(target_word)
    if index != -1:
        extracted_content = input_string[index + len(target_word):]
        return extracted_content
    else:
        return None


def howtosayword():
    with mss.mss() as sct:
        mainindex = 0
        while True:
            target_word = "say"
            url = "https://api.mymemory.translated.net/get?q="
            sep = ''
            im = numpy.asarray(sct.grab(mon))
            readerresult = reader.readtext(im, detail=0)
            print("reader result ", readerresult)
            texttotranslate = sep.join(readerresult)
            print("tettotranslate ", texttotranslate)
            inputstring = texttotranslate
            print("input string ", inputstring)
            extractedword = extractword(inputstring)
            print("extracted word ", extractedword)

            if extractedword is None:
                print("could not extract through normal methods, resorting to last method")
                extractedword = extract(texttotranslate, target_word)

            url += str(extractedword)
            url += "&langpair=en|es"
            print(url)

            response = requests.get(url)
            response_json = response.json()

            translatedtext = response_json['responseData']['translatedText']
            print(translatedtext)

            if mainindex > 0:
                print("could not answer question using default settings, changing methods")
                translatedtext = removefirstword(translatedtext)
                print(translatedtext)

            with mss.mss() as scts:
                while True:
                    mon2 = {'top': 468, 'left': 652, 'width': 600, 'height': 200}
                    im2 = numpy.asarray(scts.grab(mon2))
                    options = reader.readtext(im2, detail=0)
                    print(options)
                    break

            index = 0
            for option in options:
                print(index)
                if index >= 2:
                    mainindex += 1
                if translatedtext in options[index]:
                    print("found word ", options[index])
                    writeable = index + 1
                    writeable = str(writeable)
                    pyautogui.write(writeable)
                    pyautogui.moveTo(1334, 1003, duration=1)
                    pyautogui.leftClick()
                    pyautogui.leftClick()
                    from main import mainscript
                    mainscript()
                else:
                    print("couldnt find word")
                    index += 1
