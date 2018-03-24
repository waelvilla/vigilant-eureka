from PIL import ImageGrab,ImageOps
from numpy import *
import pyautogui
import time

class Coordinates():
    champ=(1191,754) #windowed
    shop=(1560,1370) #borderless

    camps={"krugs":(2103,1342),"red":(2091,1316),"birds":(2077,1296),"wolves":(2014,1268),"blue":(2008,1239),"gromp":(1991,1229)}
    items={"machete":(600,390),"hpot":(660,390),"trinket":(730,390)}
    levelups={"q":(1050,1220),"w":(1130,1200),"e":(1200,1200),"r":(1280,1200)}
    abilities={'q':(1050,1280),"w":(1130,1280),"e":(1200,1280),"r":(1280,1280)}
    sums={'d':(1350,1280),'f':(1410,1280)}
    flames=["you're a subhuman piece of trash", "this fucking adc is brainless", "fucking monkeys all over my games", "this botlane", "/all open mid","reported","reported","report mid","gg","you're so fucking bad"]


def switchToGame():
    pyautogui.click(Coordinates.champ)
    pyautogui.mouseUp()

######  SHOPPING     #########

def clickShop():
    pyautogui.click(Coordinates.shop)
    pyautogui.mouseUp()

def toggleShop():
    pyautogui.click(Coordinates.shop)
    pyautogui.mouseUp()
    time.sleep(0.01)
    pyautogui.click(Coordinates.shop)
    pyautogui.mouseUp()

def buyItem(c):
    pyautogui.click(c)
    pyautogui.mouseUp()
    pyautogui.click(c)
    pyautogui.mouseUp()

def buyStartingItems():
    clickShop()
    buyItem(Coordinates.items["machete"])
    for i in range(3):
        buyItem(Coordinates.items["hpot"])
    buyItem(Coordinates.items["trinket"])
    clickShop()

######  GENERAL     #########
def chat(t):
    pyautogui.keyDown('enter')
    pyautogui.keyUp('enter')
    pyautogui.typewrite(t)
    time.sleep(1)
    pyautogui.keyDown('enter')
    pyautogui.keyUp('enter')
def flame():
    pass

def levelUp(s):
    pyautogui.click(Coordinates.levelups[s])
    pyautogui.mouseUp()

def use(s,x,y):
    if(s=='q' or s=='w' or s=='e' or s=='r'):
        pyautogui.click(Coordinates.abilities[s])
    elif(s=='d' or s=='f'):
        pyautogui.click(Coordinates.sums[s])

    pyautogui.mouseUp()
    pyautogui.moveTo(Coordinates.champ)
    pyautogui.moveRel(x, y)
    pyautogui.click()
    pyautogui.mouseUp()
    toggleShop()

def imageGrab():
    pass

######  Movements     #########
def clickCenter():
    pyautogui.rightClick(Coordinates.champ)
    toggleShop()

def goCamp(s):
    pyautogui.rightClick(Coordinates.camps[s])
    time.sleep(0.1)
    pyautogui.mouseUp()
    toggleShop()
    pyautogui.moveRel(-250, -716)


def killRed():
    pyautogui.moveTo(Coordinates.champ)
    use('q',100,-200)
    time.sleep(2)
    use('d',50,-50)
    time.sleep(7.2)
    use('q',50,-50)
    time.sleep(5)
    print("Red is Dead.")

def killBirds():
    levelUp('e')
    pyautogui.moveTo(Coordinates.champ)
    use('q',0,-360)
    pyautogui.rightClick()
    pyautogui.mouseUp()
    toggleShop()
    time.sleep(0.5)
    use('e',0,0)
    time.sleep(6.8)
    use('q',-50,-95)

######  RUN     #########
switchToGame()

buyStartingItems()
levelUp('q')
chat('i afk farm dont feed')
goCamp("red")
time.sleep(23.5)
killRed()
toggleShop()

#goCamp("birds")

#goCamp("wolves")
#time.sleep(7)
#killBirds()

