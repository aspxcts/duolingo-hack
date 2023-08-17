import pyautogui



def listenandhear(x, y, x2, y2):
    pyautogui.moveTo(x, y)
    pyautogui.leftClick()
    pyautogui.moveTo(x2, y2)
    pyautogui.leftClick()
    from main import mainscript
    mainscript()
