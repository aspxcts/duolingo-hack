import pyautogui

checkbutton = 1340, 1131

def listenandhear():
    pyautogui.moveTo(572, 1126)
    pyautogui.leftClick()
    pyautogui.moveTo(checkbutton)
    pyautogui.leftClick()
    pyautogui.leftClick()
    from main import mainscript
    mainscript()
