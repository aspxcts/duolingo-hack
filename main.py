import easyocr
import time
import mss
import numpy
import requests
import json
import tkinter
from QListenHear import listenandhear
from QTypeES import typeinspanish
from QFillintheblanks import fillintheblanks
from QTypeEN import typeinenglish
from QHowToSay import howtosayword

import cv2
import pyautogui

# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

duolingo_spanish_words = (
    "este, yo, tú, él, ella, usted, nosotros, vosotros, ellos, ellas, ustedes, "
    "ser, estar, tener, hacer, ir, venir, decir, ver, comer, beber, dormir, "
    "leer, escribir, hablar, escuchar, entender, aprender, querer, necesitar, "
    "poder, saber, gustar, conocer, amar, oír, vivir, trabajar, estudiar, "
    "jugar, comprar, vender, pagar, pedir, responder, preguntar, llegar, salir, "
    "entrar, seguir, dejar, pensar, sentir, llevar, traer, empezar, terminar, "
    "mirar, encontrar, perder, ayudar, buscar, esperar, usar, probar, olvidar, "
    "recordar, explicar, caminar, correr, saltar, nadar, viajar, volar, conducir, "
    "montar, subir, bajar, cruzar, recoger, organizar, limpiar, cocinar, compartir, "
    "divertirse, bailar, cantar, reír, llorar, ganar, perder, competir, jugar, "
    "practicar, ejercitar, descansar, mirar, ver, escuchar, oír, leer, escribir, "
    "hablar, conversar, entender, aprender, enseñar, creer, opinar, soñar, desear, "
    "esperar, necesitar, querer, amar, gustar, preferir, saber, conocer, estar, "
    "sentir, ser, tener, haber, hacer, decir, ver, dar, ir, venir, saber, poder, "
    "poner, salir"
)

duolingo_spanish_words2 = (
    "dónde maleta yo dos este hermanas tú él ella usted nosotros vosotros ellos ellas ustedes "
    "ser estar tener hacer ir venir decir ver comer beber dormir "
    "leer escribir hablar escuchar entender aprender querer necesitar "
    "poder saber gustar conocer amar oír vivir trabajar estudiar "
    "jugar comprar vender pagar pedir responder preguntar llegar salir "
    "entrar seguir dejar pensar sentir llevar traer empezar terminar "
    "mirar encontrar pasaporte perder ayudar buscar esperar usar probar olvidar "
    "recordar explicar caminar correr saltar nadar viajar volar conducir "
    "montar subir bajar cruzar recoger organizar limpiar cocinar compartir "
    "divertirse bailar cantar reír llorar ganar perder competir practicar "
    "ejercitar descansar creer opinar soñar desear preferir conocer "
    "sentir tener haber hacer poder dar estar ir decir contar caer "
    "nacer morir matar gustar molestar enamorar preocupar gustar "
    "parecer costar tocar abrazar besar escribir coger solucionar "
    "resolver despedir saludar esperar alquilar comprar cerrar "
    "abrir respetar acostar enfrentar enseñar aprender llamar gritar "
    "hablar ver jugar bailar estudiar trabajar comer beber vivir "
    "viajar cocinar dormir conocer escuchar gustar pensar hacer "
    "necesitar querer tener ser estar ir venir decir ver dar "
    "saber poder poner salir buscar encontrar pedir llevar traer "
    "esperar entrar seguir dejar oír escribir creer recibir "
    "sentir hacer conocer dejar amar mirar cambiar ayudar comer "
    "esperar llamar comprar vender tomar hablar estudiar trabajar "
    "empezar terminar jugar vivir correr caminar saltar cantar "
    "bailar viajar visitar nadar manejar jugar practicar dormir "
    "enseñar aprender leer escribir entender querer gustar "
    "necesitar saber poder hablar escuchar dar conocer creer "
    "preguntar contestar pensar sentir ver buscar encontrar "
    "trabajar comprar vender pedir esperar llamar estar hacer "
    "jugar caminar correr estudiar comer beber vivir viajar "
    "enseñar aprender hablar escuchar entender querer gustar "
    "necesitar saber poder escribir cantar bailar nadar manejar "
    "trabajar comprar vender pedir comer correr estudiar "
    "jugar aprender enseñar vivir gustar necesitar saber "
    "hablar escuchar entender querer viajar bailar cantar "
    "enseñar escribir leer ver estudiar comer trabajar "
    "nadar hablar dormir escuchar correr empezar terminar "
    "subir bajar abrir cerrar buscar encontrar vivir "
    "morir matar gustar parecer costar llevar traer "
    "pensar sentir hacer conocer dejar amar llamar"
)

listeninghearing = ("Type what you hear")
writeinspanish = ("Write this in Spanish")
fillintheblanks = ("Fill In The blank")
writeinenglish = ("Write this in English")
howtosay = ("How do you say")
whichone = ("Which one of these is")
selectpairs = ("Select the matching pairs")

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
                    print("found phrase: listeninghearing: T", listeninghearing)
                    listenandhear(579, 1007, 1333, 1002)
                if writeinspanish in result:
                    print("found phrase: writeinspanish: ", writeinspanish)
                    typeinspanish()
                if fillintheblanks in result:
                    print("found phrase: fillintheblanks: ", fillintheblanks)
                    fillintheblanks()
                if writeinenglish in result:
                    print("found phrase: writeinenglish: ", writeinenglish)
                    typeinenglish()
                if howtosay in result:
                    print("found phrase: howtosay: ", howtosay)
                    howtosayword()
                else:
                    print("could not find word")
                    index += 1
            time.sleep(0.2)
