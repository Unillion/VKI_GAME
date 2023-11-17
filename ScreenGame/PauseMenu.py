from Button import Buttons
import pygame
from Settings import *
pygame.init()


def drawPause(screen, button):
    pause = pygame.Surface((H * 2, W * 2))
    pause.fill((0,0,0))
    pause.set_alpha(100)
    screen.blit(pause, (0,0))
    button.draw()
    pygame.display.update()