import pygame
from pygame.draw import circle
from pygame.draw import rect
from random import randint
import pygame.freetype
pygame.init()

pygame.mixer.music.load('music.ogg')
pygame.mixer.music.play(-1)
FPS = 60
screen = pygame.display.set_mode((1200, 900))

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
#список всех бонусов
g=[]
tick=0
pygame.font.init()
myfont = pygame.freetype.SysFont('Comic Sans MS', 30)
myfont_bonus = pygame.freetype.SysFont('Comic Sans MS', 20)

class Shar:
    def __init__(self,x,y,r,speedx,speedy,color):
        self.x = x
        self.y = y
        self.r = r
        self.speedx = speedx
        self.speedy = speedy
        self.color = color
    def move(self):
        '''
        передвигаем шарики
        '''
        if self.x<self.r or self.x>1200-self.r:
            self.speedx=-self.speedx
        if self.y<self.r or self.y>900-self.r:
            self.speedy=-self.speedy
        self.x=self.x+self.speedx   
        self.y=self.y+self.speedy
        circle(screen, self.color, (self.x, self.y), self.r)
    def demolish(self,event):
        '''
        проверяем попадание
        '''
        return((event.pos[0]-self.x)**2+(event.pos[1]-self.y)**2<=(self.r)**2)
            
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
        if self.y<0 or self.y>900-self.r:
            self.speedy=-self.speedy
        self.x=self.x+self.speedx   
        self.y=self.y+self.speedy
        if tick%15==0:
            c=self.color1
            self.color1 = self.color2
            self.color2 = c
        
        rect(screen, self.color1, (self.x, self.y, self.r,self.r))
        myfont_bonus.render_to(screen,(self.x+23,self.y+50), self.text,self.color2)
    def demolish(self,event):
        '''
        проверяем попадание
        '''
        return(event.pos[0]>self.x and event.pos[0]<self.x+self.r and event.pos[1]>self.y and event.pos[1]<self.y+self.r)   

def score():
    '''
    сохраняем имя в таблицу рекордов
    '''
    output = open('score.txt', 'a')
    print('Введите ваше имя')
    name=input()
    print(s, ' - ', name, file=output)
    output.close()

def end(f,finished):
    '''
    проверяем условие проигрыша
    '''
    if len(f)>9:
        finished = True
    return(finished)
              
pygame.display.update()
clock = pygame.time.Clock()
finished = False
while not finished:
	clock.tick(FPS)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			finished = True
		elif event.type == pygame.MOUSEBUTTONDOWN:
			for i in range (len(f)-1,-1,-1):
				if f[i].demolish(event) is True:
					f.remove(f[i])
					s=s+1
			for i in range (len(g)-1,-1,-1):
				if g[i].demolish(event) is True:
					g.remove(g[i])
					s=s+5
	if tick%45 == 0:
		f.append(Shar(randint(100,1100),randint(100,800),
			    randint(35,50),randint(5,8)*(-1)**randint(0,1),
                            randint(5,8)*(-1)**randint(0,1),COLORS[randint(0, 5)]))
	if tick%400 == 0:
		g.append(Bonus(randint(150,1050),randint(150,750),
                               randint(115,115),randint(0,1)*randint(4,7)*(-1)**randint(0,1),
                               randint(4,7)*(-1)**randint(0,1),COLORS[0],COLORS[2],'BONUS'))
	for i in range (len(f)):
		f[i].move()
	for i in range (len(g)):
		g[i].move()
	myfont.render_to(screen,(50,50), 'Score: '+str(s)+' Не допустите появления 10 и более шаров','white')
	finished=end(f,finished)
	pygame.display.update()
	screen.fill(BLACK)
	tick=tick+1
pygame.quit()
score()
