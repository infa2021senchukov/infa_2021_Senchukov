import pygame
import math as m
from pygame.draw import circle
from pygame.draw import polygon
from pygame.draw import rect
from pygame.draw import line
from pygame.draw import arc
from random import randint
import math as m
import pygame.freetype
pygame.init()

FPS = 60
screen_height=600
screen_width=1200
screen = pygame.display.set_mode((screen_width, screen_height))
tick=0

RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]
f=[]

class Sword:
    def __init__(self,l,phi,sharp,owner):
        self.l = l
        self.phi = phi
        self.sharp = sharp
        self.owner = owner
    def strike(self):
        self.phi = 5*m.pi/12
        self.sharp = 1
class Bow:
    def __init__(self,w,h,phi,tension,owner):
        self.h = h
        self.w = w
        self.phi = phi
        self.tension = tension
        self.owner = owner
    def pull(self):
        if self.owner.weapon == 'bow':
            self.tension = 0.1
    def draw(self):
        if self.owner.weapon == 'bow':
            f.append(Arrow(self.owner.x+self.owner.width,self.owner.y+self.owner.height/2,self.tension/3+10))
            self.tension = 0
class Arrow:
    def __init__(self,x,y,speed):
        self.x = x
        self.y = y
        self.speed = speed
    def fly(self):
        self.x=self.x+self.speed
        line(screen,(0,0,0),(self.x,self.y),(self.x+20,self.y),3)
class Unit:
    def __init__(self,x,y,width,height,Vx,Vy,dV,hp,weapon,buttons):
        self.x=x
        self.y=y
        self.width=width
        self.height=height
        self.Vx=Vx
        self.Vy=Vy
        self.dV=dV
        self.hp=hp
        self.weapon = weapon
        self.buttons=buttons
    def stay(self):
        '''
        отрисовываем танк
        '''
        rect(screen,'grey',(self.x,self.y,self.width,self.height))
        rect(screen,'green',(self.x+0.25*self.width,self.y+self.height+5,self.width*0.5*self.hp/100+1,10))
        rect(screen,'red',(self.x+0.25*self.width+self.width*0.5*self.hp/100,self.y+self.height+5,self.width*0.5*(100-self.hp)/100+1,10))
        if self.weapon == 'sword':
            self.hold_a_sword(sword)
        if self.weapon == 'bow':
            self.hold_a_bow(bow) 
    def change_direction(self,event):
        '''
        передвигаем юнита
        '''
        if event.type == pygame.KEYDOWN:
            if event.unicode == str(self.buttons[2]):
                self.Vx -= self.dV
            if event.unicode == str(self.buttons[3]):
                self.Vx += self.dV
            if event.unicode == str(self.buttons[0]):
                self.Vy -= self.dV
            if event.unicode == str(self.buttons[1]):
                self.Vy += self.dV
        if event.type == pygame.KEYUP:
            if event.unicode == str(self.buttons[2]):
                self.Vx += self.dV
            if event.unicode == str(self.buttons[3]):
                self.Vx -= self.dV
            if event.unicode == str(self.buttons[0]):
                self.Vy += self.dV
            if event.unicode == str(self.buttons[1]):
                self.Vy -= self.dV
    def move(self):
        if self.Vx == 0 or self.Vy == 0:
            self.x += self.Vx
            self.y += self.Vy
        else:
            self.Vx = self.Vx/m.sqrt(2)
            self.Vy = self.Vy/m.sqrt(2)
            self.x += self.Vx
            self.y += self.Vy
            self.Vx = self.Vx*m.sqrt(2)
            self.Vy = self.Vy*m.sqrt(2)
        if self.y<-self.height:
            self.y=screen_height-self.height
        if self.y>screen_height:
            self.y=0
        if self.x<-self.width:
            self.x=screen_width-self.width
        if self.x>screen_width:
            self.x=0
    def hold_a_sword(self,sword):
        line(screen,(0,0,0),(self.x+self.width,self.y+self.height/2),
             (self.x+self.width+sword.l*m.cos(sword.phi),
              self.y+self.height/2-sword.l*m.sin(sword.phi)),3)
        if sword.sharp == 1:
            sword.phi -= m.pi/30
        if sword.phi <= -5*m.pi/12:
            sword.sharp = 0
            sword.phi = 5*m.pi/12
    def hold_a_bow(self,bow):
        if (bow.tension > 0) and bow.tension < 100:
            bow.tension += 2.5
        arc(screen,(0,0,0),(self.x+self.width-bow.w/2,self.y+self.height/2-bow.h/2,bow.w,bow.h),-m.pi/2,m.pi/2,3)
        rect(screen,'yellow',(self.x+0.25*self.width,self.y+self.height+20,self.width*0.5*bow.tension/100+1,10))
        rect(screen,'grey',(self.x+0.25*self.width+self.width*0.5*bow.tension/100,self.y+self.height+20,self.width*0.5*(100-bow.tension)/100+1,10))
        
    def change_weapon(self):
        if self.weapon == 'sword':
           self.weapon = 'bow'
        elif self.weapon == 'bow':
           self.weapon = 'sword'
                   
pygame.display.update()
clock = pygame.time.Clock()
finished = False
hero = Unit(10,300,50,40,0,0,10,75,'sword',('w','s','a','d'))
sword = Sword(50,5*m.pi/12,0,hero)
bow = Bow(35,25,0,0,hero)
while not finished:
    clock.tick(FPS)
    hero.stay()
    hero.move()
    for i in range (len(f)):
        f[i].fly()    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.KEYDOWN:
            hero.change_direction(event)
        elif event.type == pygame.KEYUP:
            hero.change_direction(event)
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            sword.strike()
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 2:
            hero.change_weapon()
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
            bow.pull()
        elif event.type == pygame.MOUSEBUTTONUP and event.button == 3:
            bow.draw()
    pygame.display.update()
    screen.fill((255,255,255))
    tick=tick+1
pygame.quit()



