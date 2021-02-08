import pygame
from pygame.draw import *

pygame.init()  # инициализация

FPS = 30
screen_size = ss = (800, 600)
screen = pygame.display.set_mode((screen_size[0], screen_size[1]))

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (137, 207, 240)
DARK_GREEN = (0, 100, 0)

rect(screen, GREEN, (0, ss[1] // 2, ss[0], ss[1] // 2))  # трава
rect(screen, BLUE, (0, 0, ss[0], ss[1] // 2))  # небо
rect(screen, RED, (100, 250, 150, 150))  # стены дома
rect(screen, BLUE, (135, 295, 75, 75))  # окно
polygon(screen, GREEN, [(100, 250), (170, 150), (250, 250)])  # крыша

circle(screen, BLACK, (400, 70), 39)  # облака начинаются
circle(screen, WHITE, (400, 70), 37)
circle(screen, BLACK, (440, 70), 39)
circle(screen, WHITE, (440, 70), 37)
circle(screen, BLACK, (480, 70), 39)
circle(screen, WHITE, (480, 70), 37)
circle(screen, BLACK, (437, 100), 39)
circle(screen, WHITE, (437, 100), 37)
circle(screen, BLACK, (477, 100), 39)
circle(screen, WHITE, (477, 100), 37)  # облака заканчтваются

# содание солнышка


def pol_to_rect(angle, length):
    from math import sin, cos
    return length * cos(angle) + 630, length * sin(angle) + 100


inner_circle = []
outside_circle = []
from math import pi
sun_radius = 55
i = 0

while i < 2 * pi:
    inner_circle.append(pol_to_rect(i, sun_radius))
    i += pi / 6

i = - pi / 12
while i < 2 * pi:
    outside_circle.append(pol_to_rect(i, sun_radius + 35))
    i += pi / 6

k = 0
t = 0
merged = []
for i in range(len(inner_circle) + len(outside_circle)):
    if t < len(outside_circle):
        merged.append(outside_circle[t])
        t += 1
    if k < len(inner_circle):
        merged.append(inner_circle[k])
        k += 1

polygon(screen, YELLOW, merged, 0)

rect(screen, (0, 70, 0), (550, 220, 20, 275))  # ствол дерева

circle(screen, BLACK, (555, 220), 32)
circle(screen, DARK_GREEN, (555, 220), 30)

circle(screen, BLACK, (555, 280), 32)
circle(screen, DARK_GREEN, (555, 280), 30)

circle(screen, BLACK, (585, 240), 32)
circle(screen, DARK_GREEN, (585, 240), 30)

circle(screen, BLACK, (525, 240), 32)
circle(screen, DARK_GREEN, (525, 240), 30)

clock = pygame.time.Clock()
pygame.display.update()  # отображение элементов на экране

finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
