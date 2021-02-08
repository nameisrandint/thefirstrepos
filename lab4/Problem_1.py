import pygame
from pygame.draw import *

pygame.init() # инициализация

FPS = 30
screen_size = (800, 600)
screen = pygame.display.set_mode((screen_size[0], screen_size[1]))

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
RED = (255, 0, 0)

rect(screen, WHITE, (0, 0, screen_size[0], screen_size[1]))
circle(screen, YELLOW, (screen_size[0] // 2, screen_size[1] // 2), 250, 0)  # голова
circle(screen, BLACK, (screen_size[0] // 2, screen_size[1] // 2), 250, 3)  # контур головы
circle(screen, RED, (screen_size[0] // 2 - 90, screen_size[1] // 2 - 90), 50, 50)  # глаз
circle(screen, BLACK, (screen_size[0] // 2 - 90, screen_size[1] // 2 - 90), 25, 25)  # зрачок
circle(screen, RED, (screen_size[0] // 2 + 90, screen_size[1] // 2 - 90), 50, 50)  # глаз
circle(screen, BLACK, (screen_size[0] // 2 + 90, screen_size[1] // 2 - 90), 25, 25)  # зрачок
rect(screen, BLACK, (300, 370, 200, 30))  # рот
polygon(screen, BLACK, [(300, 103), (380, 162), (368, 178), (287, 119)], 0) # левая бровь
polygon(screen, BLACK, [(500, 103), (580, 162), (568, 178), (487, 119)], 0)  # правая бровь



clock = pygame.time.Clock()
pygame.display.update() #отображение элементов на экране

finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
