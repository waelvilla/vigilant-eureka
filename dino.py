from PIL import ImageGrab,ImageOps
import pyautogui
import time
from numpy import *
class Coordinates():
     replayBtn=(640,780)
     dino=(441,789)
    #358(418), y812, 537
def restartGame():
    pyautogui.click(Coordinates.replayBtn)

def pressSpace():
    pyautogui.keyDown('space')
    time.sleep(0.05  )
    print("Jump")
    pyautogui.keyUp('space')

def pressDown():

    print('down')
    pyautogui.keyUp('dowm')

def imageGrab():
    box=(Coordinates.dino[0] + 60, Coordinates.dino[1], Coordinates.dino[0] + 100, Coordinates.dino[1] + 40)
    image=ImageGrab.grab(box)
    grayImage=ImageOps.grayscale(image)
    a=array(grayImage.getcolors())
    return   (a.sum())
def rest():
    box=(Coordinates.replayBtn[0], Coordinates.replayBtn[1], Coordinates.replayBtn[0] + 10, Coordinates.replayBtn[1] + 10)
    im=ImageGrab.grab(box)
    grayImage=ImageOps.grayscale(im)
    a=array(grayImage.getcolors())
    return (a.sum())
def main():
    restartGame()
    while True:
        #pyautogui.keyDown('down')
       # time.sleep(0.01)
        if(imageGrab()!=1847):
        #    pyautogui.keyUp('down')
            pressSpace()
            print((Coordinates.replayBtn[0] - (Coordinates.replayBtn[0] + 10)))
            #time.sleep(0.05)


def g():
    restartGame()
    while True:
        print (imageGrab() )

main ()
#g()
