import pygame
from pygame.draw import circle
from random import randint
import pygame.freetype
pygame.init()

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
#массив всех шариков   
f=[]
tick=0
pygame.font.init()
myfont = pygame.freetype.SysFont('Comic Sans MS', 30)


def new_ball(f):
    '''
    создаем шарик
    '''
    global x,y,r
    x = randint(100,1100)
    y = randint(100,800)
    r = randint(30,50)
    speedx=randint(5,8)*(-1)**randint(0,1)
    speedy=randint(5,8)*(-1)**randint(0,1)
    color = COLORS[randint(0, 5)]
    if tick%45==0:
        circle(screen, color, (x, y), r)
        f=f.append([x,y,r,color,speedx,speedy])
        
def score():
    '''
    сохраняем имя в таблицу рекордов
    '''
    output = open('score.txt', 'a')
    print('Введите ваше имя')
    name=input()
    print(s, ' - ', name, file=output)
    output.close()
    
def move(f):
    '''
    передвигаем шарики и изменяем счет
    '''
    for i in range (len(f)):
        if f[i][0]<f[i][2] or f[i][0]>1200-f[i][2]:
            f[i][4]=-f[i][4]
        if f[i][1]<f[i][2] or f[i][1]>900-f[i][2]:
            f[i][5]=-f[i][5]
        f[i][0]=f[i][0]+f[i][4]    
        f[i][1]=f[i][1]+f[i][5]
        circle(screen, f[i][3], (f[i][0], f[i][1]), f[i][2])
    myfont.render_to(screen,(50,50), 'Score: '+str(s),'white')
        
                
        
def demolish(f,event,s):
    '''
    убираем с экрана шарик и увеличиваем счет
    '''
    for i in range (len(f)):
        if ((event.pos[0]-f[i][0])**2+(event.pos[1]-f[i][1])**2<=(f[i][2])**2):
            f[i]=[0,0,0,0,0,0]
            s=s+1
    return(s)
            
pygame.display.update()
clock = pygame.time.Clock()
finished = False
while not finished:
	clock.tick(FPS)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			finished = True
		elif event.type == pygame.MOUSEBUTTONDOWN:
			s=demolish(f,event,s)
	new_ball(f)
	tick=tick+1
	move(f)
	pygame.display.update()
	screen.fill(BLACK)

pygame.quit()
score()
