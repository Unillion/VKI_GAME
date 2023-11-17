import pygame
from Button import Buttons
from Settings import *
pygame.init()

images = [pygame.image.load('assets/level_one.png'),
            pygame.image.load('assets/level_two.png'),
            pygame.image.load('assets/level_three.png'),
            pygame.image.load('assets/level_four.png')]

def createButtonList(screen, images):
    levelButtons = []
    x = 20
    y = 200

    for image in images:
        x = x + 200
        if y < 300:
            y = y + 100
        else:
            y = y - 100
        level_one_button = Buttons(x, y, screen, image)
        levelButtons.append(level_one_button)
    return levelButtons


def drawMenu(screen, listOfButtons):
    surface = pygame.Surface((H * 2, W * 2))
    surface.fill((0,0,0))

    screen.blit(surface, (0,0))

    for button in listOfButtons:
        button.draw()
    pygame.display.update()


