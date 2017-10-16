#Clay Kynor
#10/16/17
#colorChangeWindow.py

from random import randint
from ggame import *

def mouseClick(event):
    num = randint(1,4)
    if num == 1:
        red = Color(0xff0000,1)
        line = LineStyle(3,red)
        rectangle = RectangleAsset(400,400,line,red)
    elif num == 2:
        blue = Color(0x0000ff,1)
        line = LineStyle(3,blue)
        rectangle = RectangleAsset(400,400,line,blue)
    elif num == 3:
        green = Color(0x00ff00,1)
        line = LineStyle(3,green)
        rectangle = RectangleAsset(400,400,line,green)
    elif num == 4:
        yellow = Color(0xffff00,1)
        line = LineStyle(3,yellow)
        rectangle = RectangleAsset(400,400,line,yellow)
    Sprite(rectangle)

App().listenMouseEvent("click",mouseClick)
App().run()