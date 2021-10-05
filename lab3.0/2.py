import pygame
from pygame import Color, transform
from pygame.draw import *
pygame.init()

FPS = 30
screen = pygame.display.set_mode((600, 800))
scha = pygame.Surface((600, 550), Color(1, 1, 1))
#рисуем крыло
def kr(x, y,b,c):
    skr = pygame.Surface((300, 400), Color(1, 1, 1))
    polygon(skr, (255, 255, 255), ((288, 216), (266, 168), (250, 147), (241, 135), (218, 131), (135, 132), (105, 129),(70, 121), (46, 112), (8, 91), (0, 90), (45, 157), (131, 172), (141, 181), (159, 201), (176, 218), (211, 239),), 0)
    polygon(skr, (0, 0, 0), ((288, 216), (266, 168), (250, 147), (241, 135), (218, 131), (135, 132), (105, 129),(70, 121), (46, 112), (8, 91), (0, 90), (45, 157), (131, 172), (141, 181), (159, 201), (176, 218), (211, 239),), 2)
    skr = transform.rotozoom(skr, b, c)
    scha.blit(skr, (x, y))
#рисуем клюв
def kl(x, y, b,c):
    skl = pygame.Surface((100, 30), Color(1, 1, 1))
    polygon(skl, (255, 221, 85), ((0, 15), (62, 22),(76, 5), (40, 10), (4, 0)), 0)
    polygon(skl, (0, 0, 0), ((0, 15), (62, 22),(76, 5), (40, 10), (4, 0)), 2)
    skl=transform.rotozoom(skl, b, c)
    skl2=transform.flip(skl,False, True)
    scha.blit(skl, (x, y))
    scha.blit(skl2, (x, y-10))
#рисуем хвост
def hv(x,y,b,c):
    shv = pygame.Surface((300, 350), Color(1, 1, 1))
    polygon(shv, (255, 255, 255), ((113, 285),(136, 208), (226, 309), (156, 302)), 0)
    polygon(shv, (0, 0, 0), ((113, 285),(136, 208), (226, 309), (156, 302)), 1)
    shv = transform.rotozoom(shv, b, c)
    scha.blit(shv, (x, y))
#рисуем лапы
def la(x, y,b,c):
    sla = pygame.Surface((81, 63), Color(1, 1, 1))
    polygon(sla, (255, 230, 128), ((8, 28), (12, 63), (19, 29), (27, 21), (35, 21),(76, 39), (56, 23), (42, 21), (53, 18), (81, 29), (60, 15), (42, 14), (52, 11), (69, 11), (78, 16), (74, 8), (63, 2), (47, 2), (24, 12)), 0)
    polygon(sla, (0, 0, 0), ((8, 28), (12, 63), (19, 29), (27, 21), (35, 21),(76, 39), (56, 23), (42, 21), (53, 18), (81, 29), (60, 15), (42, 14), (52, 11), (69, 11), (78, 16), (74, 8), (63, 2), (47, 2), (24, 12)), 1)
    sla = transform.rotozoom(sla, b, c)
    scha.blit(sla, (x, y))
#рисуем тело
def te(x,y):
    ste = pygame.Surface((600, 500), Color(1, 1, 1))
    ste2 = pygame.Surface((140, 150), Color(1, 1, 1))
    ellipse(ste2, (255, 255, 255), (10, 30, 110, 30), 0)
    ellipse(ste2, (255, 255, 255), (30, 0, 110, 30), 0)
    ste2 = transform.rotozoom(ste2, -15, 1)
    ste.blit(ste2,(300,373))
    ste1 = pygame.Surface((100, 150), Color(1, 1, 1))
    ellipse(ste1, (255, 255, 255), (0, 5, 40, 120), 0)
    ellipse(ste1, (255, 255, 255), (30, 0, 40, 120), 0)
    ste1 = transform.rotozoom(ste1, 30, 1)
    ste.blit(ste1,(260,270))
    ellipse(ste, (255, 255, 255), (200, 240, 205, 95), 0)
    ellipse(ste, (255, 255, 255), (362, 256, 104, 46), 0)
    ellipse(ste, (255, 255, 255), (440, 243, 75, 46), 0)
    ellipse(ste, (0, 0, 0), (484, 255, 15, 12), 0)
    scha.blit(ste, (x, y))
hv(0,15,0,1)
kr(50,20,-15,1)
kr(25,75,0,1)
kl(500,276,0,1)
la(440,430,0,1)
la(415,455,0,1)
te(0,20)
#рисуем рыбу
def ry(x, y, b, c):
    sry = pygame.Surface((220, 115), Color(1, 1, 1))
    polygon(sry, (102, 99, 112), ((160, 60),(171, 58), (196, 73), (168, 88)), 0)
    arc(sry, (71, 136, 147), (65, 33, 148, 50), 0.4, 2.74,25)
    arc(sry, (71, 136, 147), (65, 13, 148, 50), 3.44, 6,25)
    polygon(sry, (71, 136, 147), ((67, 45),(14, 80), (4, 35)), 0)
    polygon(sry, (102, 99, 112), ((135, 33), (94, 0), (164, 15),(172, 24), (171, 35)), 0) 
    polygon(sry, (102, 99, 112), ((97, 59),(80, 79), (112, 84), (114, 62)), 0) 
    circle(sry, (2, 57, 147), (170, 47), 7, 0)
    circle(sry, (5, 64, 85), (170, 47), 5, 0)
    sry = transform.rotozoom(sry, b, c)
    screen.blit(sry, (x, y))
#рисуем птичку
def pt(x, y,b,c):
    spt = pygame.Surface((200,100), Color(1, 1, 1))
    arc(spt, (255, 255, 255), (0, 0, 100, 50), 0.1, 3.04, 3)
    arc(spt, (255, 255, 255), (100, 0, 100, 50), 0.1, 3.04, 3)
    spt = transform.rotozoom(spt, b, c)
    screen.blit(spt, (x, y))
rect(screen, (33, 33, 120), (0, 0, 600, 80))
rect(screen, (141, 95, 211), (0, 80, 600, 40))
rect(screen, (205, 135, 222), (0, 120, 600, 80))
rect(screen, (222, 135, 170), (0, 200, 600, 110))
rect(screen, (255, 153, 85), (0, 310, 600, 100))
rect(screen, (0, 102, 128), (0, 410, 600, 390))
scha=transform.rotozoom(scha, 0, 0.63)
screen.blit(scha,(0,350))
ry(250,650,0,0.8)
pt(60, 0,20,0.9)
pt(300, 130,0,0.9)
pt(100, 220,-20,0.9)
pygame.display.update()
clock = pygame.time.Clock()
finished = False
while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
