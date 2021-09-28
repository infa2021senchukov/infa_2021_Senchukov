import pygame
from pygame.draw import *

pygame.init()

FPS = 30 
screen = pygame.display.set_mode((400, 400))
screen.fill((217,217,217))
#rect(screen, (255, 0, 255), (100, 100, 200, 200)) 
#rect(screen, (0, 0, 255), (100, 100, 200, 200), 5) 
#polygon(screen, (255, 255, 0), [(100,100), (200,50), (300,100), (100,100)])
 
#polygon(screen, (0, 0, 255), [(100,100), (200,50), (300,100), (100,100)], 5)
 
circle(screen, (251, 251, 4), (200, 200), 100)
circle(screen, (0, 0, 0), (200, 200), 102, 2) 
circle(screen, (255, 0, 0), (150, 175), 20)
circle(screen, (0, 0, 0), (150, 175), 7)
circle(screen, (0, 0, 0), (150, 175), 21,2)
circle(screen, (255, 0, 0), (250, 175), 15)
circle(screen, (0, 0, 0), (250, 175), 7)
circle(screen, (0, 0, 0), (250, 175), 16,2)
rect(screen, (0, 0, 0), (150, 260, 100, -15))     
#circle(screen, (255, 255, 255), (200, 175), 49, 5)

pygame.display.update() 
clock = pygame.time.Clock() 
finished = False

while not finished:
	clock.tick(FPS) 
	for event in pygame.event.get(): 
		if event.type == pygame.QUIT: 
			finished = True

pygame.quit()
