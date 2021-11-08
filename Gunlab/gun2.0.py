import pygame
from pygame.draw import circle
from pygame.draw import polygon
from pygame.draw import rect
from random import randint
import math as m
import pygame.freetype
pygame.init()

FPS = 60
screen = pygame.display.set_mode((1200, 600))

RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]
#список всех целей
f=[]
k=[]
#список всех пуль
g=[]
h=[]
tick=0
#счет
s1=0
s2=0
pygame.font.init()
myfont_bonus = pygame.freetype.SysFont('Comic Sans MS', 20)
myfont = pygame.freetype.SysFont('Comic Sans MS', 30)

class Bonus:
    def __init__(self,x,y,r,speedx,speedy,color1,color2,text):
        self.x = x
        self.y = y
        self.r = r
        self.text = text
        self.speedx = speedx
        if speedx==0:
            self.speedy = speedy
        else:
            self.speedy = 0
        self.color1 = color1
        self.color2 = color2
        
    def move(self):
        '''
        передвигаем бонусы
        '''
        if self.x<0 or self.x>1200-self.r:
            self.speedx=-self.speedx
        if self.y<0 or self.y>600-self.r:
            self.speedy=-self.speedy
        self.x=self.x+self.speedx   
        self.y=self.y+self.speedy
        if tick%15==0:
            c=self.color1
            self.color1 = self.color2
            self.color2 = c
        
        rect(screen, self.color1, (self.x, self.y, self.r,self.r))
        myfont_bonus.render_to(screen,(self.x+23,self.y+50), self.text,self.color2)

def demolish(h,g,k,s1,s2):
    '''
    удаляем бонусы
    '''
    for i in range (len(h)):
        for j in range (len(k)-1,-1,-1):
            if h[i].x<k[j].x+31+k[j].r and h[i].x>k[j].x-31 and h[i].y<k[j].y+31+k[j].r and h[i].y>k[j].y-31:
                k.remove(k[j])
                s2=s2+5
    for i in range (len(g)):
        for j in range (len(k)-1,-1,-1):
            if g[i].x<k[j].x+31+k[j].r and g[i].x>k[j].x-31 and g[i].y<k[j].y+31+k[j].r and g[i].y>k[j].y-31:
                k.remove(k[j])
                s1=s1+5
    return((s1,s2))
class Shar:
    def __init__(self,x,y,r,speedx,speedy,color,h):
        self.x = x
        self.y = y
        self.r = r
        self.speedx = speedx
        self.speedy = speedy
        self.color = color
        self.h=h
    def move(self,f,i):
        '''
        передвигаем шарики
        '''
        if (self.x<self.r+200 or self.x>1200-self.r) and f[i].h!=tick-1:
            self.speedx=-self.speedx
            f[i].h=tick
        if (self.y<self.r or self.y>600-self.r) and f[i].h!=tick-1:
            self.speedy=-self.speedy
            f[i].h=tick
        if (self.x<self.r+200 or self.x>1200-self.r or self.y<self.r or self.y>600-self.r) and f[i].h==tick-1:
            f[i].r=0
            f[i].x=3000
            f[i].y=3000
        for j in range(i+1,len(f),1):
            if ((f[j].x-f[i].x)**2+(f[j].y-f[i].y)**2<=(f[j].r+f[i].r)**2) and f[i].h!=tick-1:
                f[i].speedx=-f[i].speedx
                f[i].speedy=-f[i].speedy
                f[j].speedx=-f[j].speedx
                f[j].speedy=-f[j].speedy
                f[i].h=tick
            if ((f[j].x-f[i].x)**2+(f[j].y-f[i].y)**2<=(f[j].r+f[i].r)**2) and f[i].h == tick-1:
                f[i].r=0
                f[i].x=1000
                f[i].y=1000
        self.x=self.x+self.speedx   
        self.y=self.y+self.speedy
        circle(screen, self.color, (self.x, self.y), self.r)
class Gun:
    def __init__(self,l,y,x,phi,buttons):
        self.l = l
        self.y = y
        self.x = x
        self.phi = phi
        self.buttons = buttons
    '''
    поворачиваем пушку
    '''
    def orientation(self,tank):
        if pygame.key.get_pressed()[self.buttons[0]]:
                self.phi=self.phi+0.1
        sin=m.sin(self.phi)
        cos=m.cos(self.phi)
        if pygame.key.get_pressed()[self.buttons[1]]:
            self.l=self.l+1
        if pygame.key.get_pressed()[self.buttons[1]]== False:
            self.l=100
        self.y=tank.y+37.5-12.5*cos
        self.x=tank.x+37.5-12.5*sin
        polygon(screen,'black',[(self.x,self.y),(self.x+self.l*cos,self.y-self.l*sin),
                                    (self.x+self.l*cos+25*sin,self.y-self.l*sin+25*cos),(self.x+25*sin,self.y+25*cos)])
        return((cos,sin))
class Bullet:
    def __init__(self,vx,vy,x,y):
        self.vx = vx
        self.vy = vy
        self.x=x
        self.y=y
        '''
        двигаем пули
        '''
    def move(self,g,f):
        if self.y<15 or self.y>600-15:
            self.vy=-self.vy
        self.vy=self.vy+0.5
        self.x=self.x+self.vx   
        self.y=self.y+self.vy           
        circle(screen, (0,0,0), (self.x, self.y), 12.5)
def score():
    '''
    сохраняем имя в таблицу рекордов
    '''
    if tank1.hp>0:
        output = open('score.txt', 'a')
        print('Введите ваше имя')
        name=input()
        print(s1, ' - ', name, file=output)
        output.close()
    if tank2.hp>0:
        output = open('score.txt', 'a')
        print('Введите ваше имя')
        name=input()
        print(s2, ' - ', name, file=output)
        output.close()

def end(tick,finished):
    '''
    проверяем условие проигрыша
    '''
    if tank1.hp==0 or tank2.hp==0:
        finished = True
    return(finished)

class Tank:
    def __init__(self,x,y,hp,buttons):
        self.x=x
        self.y=y
        self.hp=hp
        self.buttons=buttons
    def stay(self):
        '''
        отрисовываем танк
        '''
        rect(screen,'grey',(self.x,self.y,75,75))
        rect(screen,'green',(self.x+12.5,self.y+80,self.hp/2+1,10))
        rect(screen,'red',(self.x+12.5+self.hp/2,self.y+80,50-self.hp/2,10))
        
    def move(self,event):
        '''
        передвигаем танк
        '''
        if pygame.key.get_pressed()[self.buttons[0]]:
            self.y=self.y-5
        if pygame.key.get_pressed()[self.buttons[1]]:
            self.y=self.y+5
        if self.y<-75:
            self.y=525
        if self.y>600:
            self.y=0
    def damage(self,h,tank):
        '''
        от попаданий танк получает урон
        '''
        for i in range (len(h)-1,-1,-1):
            if h[i].x<tank.x+106 and h[i].x>tank.x-31 and h[i].y<tank.y+106 and h[i].y>tank.y-31:
                h.remove(h[i])
                tank.hp=tank.hp-10
                      
pygame.display.update()
clock = pygame.time.Clock()
finished = False
gun1=Gun(100,300,47.5,0,[pygame.K_q,pygame.K_a])
gun2=Gun(100,300,1077.5,m.pi,[pygame.K_i,pygame.K_k])
tank1=Tank(10,300,100,[pygame.K_w,pygame.K_s])
tank2=Tank(1115,300,100,[pygame.K_o,pygame.K_l])
while not finished:
    clock.tick(FPS)
    if tick%400 == 0:
        k.append(Bonus(randint(200,1000),randint(200,400),
                        115,randint(0,1)*randint(4,7)*(-1)**randint(0,1),
                        randint(4,7)*(-1)**randint(0,1),COLORS[0],COLORS[2],'BONUS'))
    if tick%30 == 0:
        f.append(Shar(randint(260,1140),randint(60,540),
                randint(35,50),randint(3,5)*(-1)**randint(0,1),
                        randint(3,5)*(-1)**randint(0,1),COLORS[randint(0, 5)],0))
    for i in range (len(k)):
        k[i].move()
    '''
    удаляем лишние шарики
    '''
    if len(f)>9:
	    f.remove(f[0])
    for i in range (len(f)):
        f[i].move(f,i)
    tank1.stay()
    tank2.stay()
    bonus_schet=demolish(h,g,k,s1,s2)
    s1=bonus_schet[0]
    s2=bonus_schet[1]
    tank1.damage(g,tank2)
    tank2.damage(h,tank1)
    x=gun1.orientation(tank1)
    y=gun2.orientation(tank2)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        tank1.move(event)
        tank2.move(event)
        if event.type == pygame.KEYUP:
            '''
            выстреливаем
            '''
            if event.key == gun1.buttons[1] and x!= None:
                g.append(Bullet(gun1.l*x[0]*0.35-15,-gun1.l*x[1]*0.35+15,
                                gun1.l*x[0]+12.5*x[1]+gun1.x,gun1.y-gun1.l*x[1]+25*x[0]))
            if event.key == gun2.buttons[1] and y!= None:
                h.append(Bullet(gun2.l*y[0]*0.35+15,-gun2.l*y[1]*0.35+15,
                                gun2.l*y[0]+12.5*y[1]+gun2.x,gun2.y-gun2.l*y[1]+25*y[0]))
        '''
        перезапуск
        '''
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.pos[0]>50 and event.pos[0]<150 and event.pos[1]>100 and event.pos[1]<150:
                g=[]
                f=[]
                s1=0
                s2=0
                tank1.hp=100
                tank2.hp=100
                tick=0
    for i in range (len(g)):
        g[i].move(g,f)
    for i in range (len(h)):
        h[i].move(h,f)
    for i in range (len(g)-1,-1,-1):
        if g[i].x<0:
            g.remove(g[i])
    for i in range (len(g)-1,-1,-1):
        if g[i].x<0 or g[i].x>1200:
            g.remove(g[i])
    for i in range (len(h)-1,-1,-1):
        if h[i].x<0 or h[i].x>1200:
            h.remove(h[i])
    for i in range (len(g)):
        for j in range (len(f)-1,-1,-1):
            if (f[j].x-g[i].x)**2+(f[j].y-g[i].y)**2<=(f[j].r+12.5)**2:
                f.remove(f[j])
                s1=s1+1
    for i in range (len(h)):
        for j in range (len(f)-1,-1,-1):
            if (f[j].x-h[i].x)**2+(f[j].y-h[i].y)**2<=(f[j].r+12.5)**2:
                f.remove(f[j])
                s2=s2+1
    myfont.render_to(screen,(50,50), 'Score 1: '+str(s1)+'  Score 2: '+str(s2),'Black')
    pygame.display.update()
    screen.fill((255,255,255))
    tick=tick+1
    finished=end(tick,finished)
    rect(screen,'black',(50,100,100,50))
    myfont.render_to(screen,(60,110), 'Again','White')
pygame.quit()
score()
