import easyocr
import time
import mss
import numpy
import openai

with open('C:\APIKEYS\openai.txt') as f:
    key = f.read()
with open('C:\ENDPOINTS\openai.txt') as f:
    endpoint = f.read()

openai.api_base = endpoint
openai.api_key = key

from QListenHear import listenandhear
from QTypeES import typeinspanish
from QFillintheblanks import fillintheblanksmethod
from QTypeEN import typeinenglish
from QHowToSay import howtosayword
from QWhichOne import whichone

openai.api_type = "azure"
openai.api_version = "2023-05-15"

listeninghearing = ("Type what you hear")
speakthissentence = ("Speak this sentence")
writeinspanish = ("Write this in Spanish")
fillintheblanks = ("Fill in the blank")
writeinenglish = ("Write this in English")
howtosaykeys = ("How do you say")
whichonekeys = ("Which one of these is")
selectpairskeys = ("Select the matching pairs")

mon = {'top': 267, 'left': 585, 'width': 600, 'height': 100}
reader = easyocr.Reader(['en', 'es'])


def mainscript():
    with mss.mss() as sct:
        while True:
            im = numpy.asarray(sct.grab(mon))

            sep = ""
            readerresult = reader.readtext(im, detail=0)
            print(readerresult)
            result = sep.join(readerresult)
            print(result)

            index = 0
            while index < len(result):
                time.sleep(0.01)
                print(index)
                if len(result) <= 0:
                    break
                if listeninghearing in result:
                    print("found phrase: listeninghearing: ", listeninghearing)
                    listenandhear(579, 1007, 1333, 1002)
                if writeinspanish in result:
                    print("found phrase: writeinspanish: ", writeinspanish)
                    typeinspanish()
                if fillintheblanks in result:
                    print("found phrase: fillintheblanks: ", fillintheblanks)
                    fillintheblanksmethod()
                if writeinenglish in result:
                    print("found phrase: writeinenglish: ", writeinenglish)
                    typeinenglish()
                if howtosaykeys in result:
                    print("found phrase: howtosay: ", howtosaykeys)
                    howtosayword()
                if whichonekeys in result:
                    print("found phrase: whichone ", whichonekeys)
                    whichone()
                if speakthissentence in result:
                    print("found phrase: speakthissentence ", speakthissentence)
                    listenandhear(579, 1007, 1333, 1002)
                else:
                    print("could not find word")
                    index += 1
            time.sleep(0.2)
