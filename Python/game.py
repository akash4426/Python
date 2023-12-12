import pygame as py
import random as r
import math as m
py.init()
clock=py.time.Clock()
FPS=60
screen=py.display.set_mode((800,600))

background=py.image.load('Background.jpg').convert()
bg_width=background.get_width()
py.display.set_caption('Turle race')
scroll=0
tiles=m.ceil(800/bg_width)+1
scroll=0

#player
playerimg=py.image.load('sea-turtle.png')
playerx=370
playery=480

playery_change=0
grav=1

#enemy
enemyimg=py.image.load('crocodile.png')
enemyx=r.randint(500,800)
enemyy=480
enemyx_change=0.3
enemyy_change=0


def player(x,y):
    screen.blit(playerimg,(x,y))

def enemy(x,y):
    screen.blit(enemyimg,(x,y))
    #blit=draw
#game loop
start=True
while start:
    clock.tick(FPS)
    
    

    for event in py.event.get(): 
        if event.type==py.QUIT:
            start=False

        if event.type==py.KEYDOWN:
            if event.key == py.K_SPACE and playery_change==0:
                playery_change=14
    if playery_change>0 or playery<480:
        playery-=playery_change
        playery_change-=grav
    if playery>480:
        playery=480
    if playery ==480 and playery_change<0:
        playery_change=0


    
    

                
    screen.fill((255,255,255))
    for i in range(0,tiles):
        screen.blit(background,(i*800 + scroll,0))
    scroll -=5
    if abs(scroll)>800:
        scroll=0

  
        

    player(playerx,playery)
    enemy(enemyx,enemyy)
    
    py.display.update()