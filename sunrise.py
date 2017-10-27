#Clay Kynor
#10/27/17
#sunrise.py

from ggame import *

ROWS = 26
COLS = 50
CELL_SIZE = 20

def moveRight(event):
    if monkey.x < (COLS-1)*CELL_SIZE:
        monkey.x += CELL_SIZE
        if monkey.x == banana.x and monkey.y == banana.y:
            moveBanana()
            updateScore()

def moveLeft(event):
    if monkey.x > 0:
        monkey.x -= CELL_SIZE
        if monkey.x == banana.x and monkey.y == banana.y:
            moveBanana()
            updateScore()
    
def moveUp(event):
    if monkey.y > 0:
        monkey.y -= CELL_SIZE
        if monkey.x == banana.x and monkey.y == banana.y:
            moveBanana()
            updateScore()

def moveDown(event):
    if monkey.y < (ROWS-1)*CELL_SIZE: 
        monkey.y += CELL_SIZE
        if monkey.x == banana.x and monkey.y == banana.y:
            moveBanana()
            updateScore()
yellow = Color(0x00FF00)

def moveBanana():
    banana.x = randint(0,COLS-1)*CELL_SIZE
    banana.y = randint(0,ROWS-1)*CELL_SIZE
    data['frames'] = 0
    
def step():
    data['frames'] += 1
    if data['frames'] == 149:
        moveBanana()

yellow = Color(0xFFFF00,1)
green = Color(0x00FF00,1)

jungleBox = RectangleAsset(COLS*CELL_SIZE,ROWS*CELL_SIZE,LineStyle(1,green),green)
sun = CircleAsset(

Sprite(jungleBox)
monkey = Sprite(sun)

App().listenKeyEvent('keydown','right arrow',moveRight)
App().listenKeyEvent('keydown','left arrow',moveLeft)
App().listenKeyEvent('keydown','up arrow',moveUp)
App().listenKeyEvent('keydown','down arrow',moveDown)    
App().Run()