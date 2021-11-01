import pygame
from pygame.draw import circle
from pygame.draw import polygon
from pygame.draw import rect
from random import randint
import math as m
import pygame.freetype
pygame.init()

pygame.mixer.music.load('music.ogg')
pygame.mixer.music.play(-1)
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
#счетчик попаданий
s=0
#список всех шаров
f=[]
#список всех пуль
g=[]
tick=0
#счет
s=0
pygame.font.init()
myfont = pygame.freetype.SysFont('Comic Sans MS', 30)

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
    def __init__(self,l,tan):
        self.l = l
        self.tan = tan
    '''
    поворачиваем пушку
    '''
    def orientation(self):
        a=pygame.mouse.get_pos()
        if a[0]==0:
            cos=0
            sin=1
            k=10
        else:
            self.tan=(300-a[1])/a[0]
            cos=m.sqrt(1/(1+self.tan**2))
            if self.tan>0:
                sin=m.sqrt(1-cos**2)
            else:
                sin=-m.sqrt(1-cos**2)
        if cos!=0:
            if 1/cos >6:
                k=6
        if cos!=0:
            if 1/cos<6:
                k=1/cos
        t = pygame.mouse.get_pressed()
        if t[0] == True:
            self.l=self.l+1
        if t[0]== False:
            self.l=100
        polygon(screen,'black',[(0,300),(self.l*cos,300-self.l*sin),
                                (self.l*cos+25*sin,300-self.l*sin+25*cos),(0,300+25*k)])
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
    def move(self,g,f, gun):
        if self.x>1200-12.5:
            self.vx=-self.vx
        if self.y<12.5 or self.y>600-12.5:
            self.vy=-self.vy
        self.vy=self.vy+0.5
        self.x=self.x+self.vx   
        self.y=self.y+self.vy
        circle(screen, (0,0,0), (self.x, self.y), 12.5)
def score():
    '''
    сохраняем имя в таблицу рекордов
    '''
    output = open('score.txt', 'a')
    print('Введите ваше имя')
    name=input()
    print(s, ' - ', name, file=output)
    output.close()

def end(tick,finished):
    '''
    проверяем условие проигрыша
    '''
    if 90-tick/60<0:
        finished = True
    return(finished)
         
pygame.display.update()
clock = pygame.time.Clock()
finished = False
gun=Gun(100,0)
while not finished:
    clock.tick(FPS)
    if tick%30 == 0:
        f.append(Shar(randint(260,1140),randint(60,540),
                randint(35,50),randint(3,5)*(-1)**randint(0,1),
                        randint(3,5)*(-1)**randint(0,1),COLORS[randint(0, 5)],0))
    '''
    удаляем лишние шарики
    '''
    if len(f)>9:
	    f.remove(f[0])
    for i in range (len(f)):
        f[i].move(f,i)
    x=gun.orientation()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        if event.type == pygame.MOUSEBUTTONUP:
            g.append(Bullet(gun.l*x[0]*0.35-15,-gun.l*x[1]*0.35+15,
                            gun.l*x[0]+12.5*x[1],300-gun.l*x[1]+25*x[0]))
        '''
        перезапуск
        '''
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.pos[0]>50 and event.pos[0]<150 and event.pos[1]>100 and event.pos[1]<150:
                g=[]
                f=[]
                s=0
                tick=0
    for i in range (len(g)):
        g[i].move(g,f, gun)
    for i in range (len(g)-1,-1,-1):
        if g[i].x<0:
            g.remove(g[i])
    for i in range (len(g)):
        for j in range (len(f)-1,-1,-1):
            if (f[j].x-g[i].x)**2+(f[j].y-g[i].y)**2<=(f[j].r+12.5)**2:
                f.remove(f[j])
                s=s+1
    myfont.render_to(screen,(50,50), 'Score: '+str(s)+' Time left:'+str(int((90-tick/60))),'Black')
    pygame.display.update()
    screen.fill((255,255,255))
    tick=tick+1
    finished=end(tick,finished)
    rect(screen,'black',(50,100,100,50))
    myfont.render_to(screen,(60,110), 'Again','White')
pygame.quit()
score()
