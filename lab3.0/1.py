import pygame
from pygame import Color, transform
from pygame.draw import *
pygame.init()

FPS = 30
screen = pygame.display.set_mode((300, 300))
rect(screen,(194,197,204),(0,0,300,300))
circle(screen,(255,255,0),(150,150),50)
circle(screen,(0,0,0),(150,150),50,2)
circle(screen,(221,0,1),(130,135),15)
circle(screen,(0,0,0),(130,135),15,2)
circle(screen,(0,0,0),(130,135),6)
circle(screen,(221,0,1),(170,135),11)
circle(screen,(0,0,0),(170,135),11,2)
circle(screen,(0,0,0),(170,135),5)
rect(screen,(0,0,0),(125,170,50,10))
polygon(screen, (0, 0, 0), ((110, 95),(150, 125), (145, 130), (105, 100)))
polygon(screen, (0, 0, 0), ((155, 125),(160, 130),(195, 105), (190, 100)))
pygame.display.update()
clock = pygame.time.Clock()
finished = False
while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
