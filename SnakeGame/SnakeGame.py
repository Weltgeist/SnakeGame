#import pygame
#
#(width,height)=(300,200)
#screen=pygame.display.set_mode((width,height))
#pygame.display.flip()

# -*- coding: utf-8 -*-
"""
Created on Sun Mar 10 22:55:26 2019

@author: Weltgeist-Samuel Narcisse
"""
import colors
import math
import random
import pygame
from pygame import *
from pygame.locals import *
#from pygame.locals import *
#import tkinter as tk
#from tkinter import messagebox

class cube(object):
        rows=20
        w=500
        def __init__(self,start,dirnx=1,dirny=0,color=(255,0,0)):
            self.pos=start
            self.dirnx=1 ##Start snake moving
            self.dirny=0
            self.color=color
            
        def move(self,dirnx,dirny):
            self.dirnx=dirnx
            self.dirny=dirny
            self.pos=(self.pos[0]+self.dirnx,self.pos[1]+self.dirny)
            
        def draw(self,surface,eyes=False):
            dis=self.w//self.rows
            i=self.pos[0]
            j=self.pos[1]
            
            pygame.draw.rect(surface,self.color,(i*dis+1,j*dis+1,dis-2,dis-2))
            if eyes:
                centre=dis//2
                radius=3
                circleMiddle1=(i*dis+centre-radius,j*dis+8)
                circleMiddle2=(i*dis+dis-radius*2,j*dis+8)
                pygame.draw.circle(surface,(0,0,0),circleMiddle1,radius)
                pygame.draw.circle(surface,(0,0,0),circleMiddle2,radius)
                
        
class snake(object):
    body=[]
    turns={}
    def __init__(self,color,pos):
        self.colors=colors
        self.head=cube(pos)
        self.body.append(self.head)
        self.dirnx=0
        self.dirny=1 #Can only move in one direction at same time
        
    def move(self):
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                exit()
                
            keys=pygame.key.get_pressed()
            
            for key in keys:
                if keys[pygame.K_LEFT]:
                    self.dirnx=-1
                    self.dirny=0
                    self.turns[self.head.pos[:]]=[self.dirnx,self.dirny] ##To know what way we turned
                elif keys[pygame.K_RIGHT]:
                    self.dirnx=1
                    self.dirny=0
                    self.turns[self.head.pos[:]]=[self.dirnx,self.dirny]
                    
                elif keys[pygame.K_UP]:
                    self.dirnx=0
                    self.dirny=-1 #Respect py games convention
                    self.turns[self.head.pos[:]]=[self.dirnx,self.dirny]
                    
                elif keys[pygame.K_DOWN]: 
                    self.dirnx=0
                    self.dirny=1
                    self.turns[self.head.pos[:]]=[self.dirnx,self.dirny]
                    
        for i, c in enumerate(self.body):
            p=c.pos[:]
            if p in self.turns:
                turn=self.turns[p]
                c.move(turn[0],turn[1])
                if i == len(self.body)-1:
                    self.turns.pop(p)
                else:##colision detector
                    if c.dirnx==-1 and c.pos[0]<=0: c.pos=(c.rows-1,c.pos[1])
                    elif c.dirnx==1 and c.pos[0]<=c.rows-1: c.pos=(0,c.pos[1])
                    elif c.dirnx==1 and c.pos[0]<=c.rows-1: c.pos=(c.pos[0],0)
                    elif c.dirnx==-1 and c.pos[0]<=0: c.pos=(c.pos[0],c.rows-1)
                    else: c.move(c.dirnx,c.dirny)
                    
    def reset(self,pos):
        pass
    def addCube(self):
        pass
    def draw(self,surface):
        for i ,c in enumerate(self.body):
            if i==0:
                c.draw(surface,True) ##add eyes for head
            else:
                c.draw(surface)
    
def drawGrid(w,rows,surface):
    sizeBetween=w//rows
    
    x=0
    y=0
    for l in range(rows):
        x=x+sizeBetween
        y=y+sizeBetween
        
        pygame.draw.line(surface,(255,255,255,),(x,0),(x,w)) #start pos and end pos
        pygame.draw.line(surface,(255,255,255,),(0,y),(w,y)) #draw line accros the screen

def redrawWindow(surface):
    global rows, width , s
    surface.fill((0,0,0))
    s.draw(surface)
    drawGrid(width,rows,surface)
    pygame.display.update()
    

def randomSnack(rows,items):
    global rows
    position=item.body
    while True:
        x= random.randrange(rows)
        y=random.randrange(rows)
        if len(list(filter(lambda z:z.pos==(x,y),positions)))>0:
            continue
        else:
            break
    return(x,y)
        

def messageBox(subject,content):
    pass
def main():
    global width, rows , s
    width=500
    rows=20
    pygame.init()
    surface=pygame.display.set_mode((width,width)) #Create a Surface //widthxheight
    pygame.display.set_caption('SnakeProgram')
    s=snake((255,0,0),(10,10))
    flag=True
    clock=pygame.time.Clock()
    while flag:
        #pygame.event.wait()
        pygame.time.delay(50) #Additional delays
        clock.tick(10) #Not faster than 10 frame per sec
        s.move()
        redrawWindow(surface)
        

    pass


main()

"""
rows=
w=
h=

cube.rows=rows
cube.w=w
"""

