import pyautogui
import mss
import sys
import re
import numpy
import easyocr
import openai
from main import key
from main import endpoint

openai.api_type = "azure"
openai.api_version = "2023-05-15"
openai.api_base = endpoint
openai.api_key = key

sentences = []
lastwordprompt = '''Which one of these sentences makes the most sense? Please respond in the following format:
Sentence number of the sentence that makes the most sense, starting from 1 (if two or more sentences make somewhat sense, pick the one that makes the most sense)
your answer should only contain a number
could you respond with nothing, not even the sentences, just the format
Here are your sentences:  
'''
middletwowordprompt = '''
Which one of these sentences makes the most sense? Please respond in the following format:
Sentence number of the sentence that makes the most sense, starting from 1 (if two or more sentences make somewhat sense, pick the one that makes the most sense)
your answer should only contain a number
could you respond with nothing, not even the sentences, just the format
Here are your sentences:  
'''
lastwordprompt = str(lastwordprompt)
middletwowordprompt = str(lastwordprompt)

checkbutton = 1340, 1131

reader = easyocr.Reader(["en", "es"])
mon = {'left': 630, 'top': 433, 'width': 600, 'height': 150}
mon2 = {'left': 781, 'top': 546, 'width': 300, 'height': 500}


def cycle_through_lists(sentence, options):
    result1 = sentence[0] + ' ' + options[0] + ' ' + sentence[1] + ' ' + options[1] + ' ' + sentence[2]
    result2 = sentence[0] + ' ' + options[1] + ' ' + sentence[1] + ' ' + options[0] + ' ' + sentence[2]
    return result1, result2


def single_last_word():
    with mss.mss() as sct:
        while True:
            im = numpy.asarray(sct.grab(mon))
            sentence = reader.readtext(im, detail=0)
            sep = ''
            sepspace = ' '
            print(sentence)
            stringsentence = sep.join(sentence)
            print(stringsentence)
            im2 = numpy.asarray(sct.grab(mon2))
            options = reader.readtext(im2, detail=0)
            print(options)
            stringoptions = sepspace.join(options)
            print(stringoptions)
            mainprompt = lastwordprompt
            for option in options:
                fullsentence = ''
                fullsentence += stringsentence
                fullsentence += ' '
                fullsentence += option
                mainprompt += fullsentence
                mainprompt += "\n"
                print(mainprompt)

            sentencecheck = openai.ChatCompletion.create(
                engine="gpt-35-turbo",
                messages=[
                    {"role": "user", "content": mainprompt}
                ]
            )
            print(sentencecheck['choices'][0]['message']['content'])
            sentencecheck = str(sentencecheck['choices'][0]['message']['content'])

            pyautogui.write(sentencecheck)
            pyautogui.moveTo(checkbutton, duration=1)
            pyautogui.leftClick()
            pyautogui.leftClick()

            from main import mainscript
            mainscript()


def double_middle_word():
    with mss.mss() as sct:
        while True:
            sep = ''
            sepspace = ' '
            im = numpy.asarray(sct.grab(mon))
            sentence = reader.readtext(im, detail=0)
            sep = ''
            sepspace = ' '
            print(sentence)
            stringsentence = sep.join(sentence)
            print(stringsentence)
            im2 = numpy.asarray(sct.grab(mon2))
            optionables = reader.readtext(im2, detail=0)
            print(optionables)
            stringoptions = sepspace.join(optionables)
            print(stringoptions)
            mainprompt = middletwowordprompt

            result1, result2 = cycle_through_lists(sentence, optionables)
            mainprompt += result1
            mainprompt += '\n'
            mainprompt += result2
            print(mainprompt)

            sentencecheck = openai.ChatCompletion.create(
                engine="gpt-35-turbo",
                messages=[
                    {"role": "user", "content": mainprompt}
                ]
            )
            print(sentencecheck['choices'][0]['message']['content'])
            sentencecheck = int(sentencecheck['choices'][0]['message']['content'])

            if sentencecheck == 1:
                writeable = optionables[0]
                print(writeable)
                pyautogui.write(writeable)
                writeable = optionables[1]
                print(writeable)
                pyautogui.write(writeable)
            if sentencecheck == 2:
                writeable = optionables[1]
                print(writeable)
                pyautogui.write(writeable)
                writeable = optionables[0]
                print(writeable)
                pyautogui.write(writeable)

            pyautogui.moveTo(checkbutton, duration=1)
            pyautogui.leftClick()
            pyautogui.leftClick()

            from main import mainscript
            mainscript()


def createsentence():
    with mss.mss() as sct:
        while True:
            url = "https://api.mymemory.translated.net/get?q="
            sep = ''
            sepspace = ' '
            im = numpy.asarray(sct.grab(mon))
            sentence = reader.readtext(im, detail=0)

            if len(sentence) == 0:
                single_last_word()
            if len(sentence) > 0:
                double_middle_word()

            # texttotranslate = sep.join(readerresult)


def fillintheblanksmethod():
    with mss.mss() as sct:
        while True:
            createsentence()

            # texttotranslate = sep.join(readerresult)
