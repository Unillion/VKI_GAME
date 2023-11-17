import pygame
from Settings import *

class Objects():
    def __init__(self, x,y, screen, image):
        self.screen = screen
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)

    def draw(self):
        self.screen.blit(self.image, (self.rect.x, self.rect.y))

def fade(screen, alpha):

    if alpha >= 0:
        pygame.time.delay(5)
        fade = pygame.Surface((H*2, W*2))
        fade.fill((0, 0, 0))

        fade.set_alpha(alpha)

        screen.blit(fade, (0, 0))

        pygame.display.update()




