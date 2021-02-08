import pygame
from pygame.draw import *

FPS = 30


def main():
    pygame.init()  # инициализация
    screen_size = ss = (800, 600)
    screen = pygame.display.set_mode((screen_size[0], screen_size[1]))

    draw_house(250, 470, 400, 250)

    clock = pygame.time.Clock()
    pygame.display.update()  # отображение элементов на экране

    finished = False

    while not finished:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finished = True

    pygame.quit()


def draw_house(x, y, hight, width):
    """
    Функция, которая рисует дом, по заданным координатам
    и заданным высоте и ширине. Точка (x, y) - это середина самого
    низа дома. От нее строися весь дом.

    :param x: абцисса
    :param y: ордината
    :param hight: высота дома, ни одна из частей дома не должна
    выходить за пределы высоты
    :param width: ширина дома, ни одна из частей дома не должна
    выходить за пределы ширины
    :return: None
    """
    pass

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (137, 207, 240)
DARK_GREEN = (0, 100, 0)

main()
