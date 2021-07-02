import pygame
from random import randint
from time import sleep


pygame.init()
width = 400
height = 400
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Bubble Sort Algorithm")
def control():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()


lines = []
for i in range(width):
    lines.append(pygame.Rect(i, 0, 1, i))
    # randint(1, height)


def ChangeIndex(list, pos1, pos2): 
    list[pos1].h, list[pos2].h = list[pos2].h, list[pos1].h
for i in range(len(lines)):
    ChangeIndex(lines, i, randint(1, len(lines)-1))

while True:
    control()
    pygame.display.update()
    window.fill((0, 0, 0))

    for i in range(len(lines)):
        pygame.draw.rect(window, (255, 255, 255), lines[i])


    for i in range(len(lines) - 1):
        if lines[i].h > lines[i + 1].h:
            first = lines[i].h
            second = lines[i + 1].h
            lines[i].h = second
            lines[i + 1].h = first
         

    sleep(0.030)