import pygame
from Settings import *

class Tiles(pygame.sprite.Sprite):
    def __init__(self, pos, size):
        super().__init__()
        self.image = pygame.Surface((size,size))
        self.image.fill('blue')
        self.rect = self.image.get_rect()
        self.rect.topleft = pos

    def update(self, x_Shift):
        self.rect.x += x_Shift

class TileUnderground(pygame.sprite.Sprite):
    def __init__(self, pos, size):
        super().__init__()
        self.image = pygame.Surface((size,size))
        self.image.fill('white')
        self.rect = self.image.get_rect()
        self.rect.topleft = pos

    def update(self, x_Shift):
        self.rect.x += x_Shift
