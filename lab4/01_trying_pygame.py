import pygame
from pygame.draw import *

FPS = 60

pygame.init()

screen = pygame.display.set_mode((300, 200))

clock = pygame.time.Clock()

while True:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
