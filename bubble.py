#Clay Kynor
#10/25/17
#bubble.py

from random import randint
from ggame import *

def mouseClick(event):
    num = randint(1,4)
    size = randint(5,50)
    if num == 1:
        red = Color(0xff0000,1)
        line = LineStyle(3,red)
        bubble = CircleAsset(size,line,red)
    elif num == 2:
        blue = Color(0x0000ff,1)
        line = LineStyle(3,blue)
        bubble = CirlceAsset(size,line,blue)
    elif num == 3:
        green = Color(0x00ff00,1)
        line = LineStyle(3,green)
        bubble = CircleAsset(size,line,green)
    elif num == 4:
        yellow = Color(0xffff00,1)
        line = LineStyle(3,yellow)
        bubble = CircleAsset(size,line,yellow)
    Sprite(bubble)

App().listenMouseEvent("click",mouseClick)
App().run()
