import pygame
import random

from pygame import BLEND_RGB_ADD

pygame.init()


class EndGem(pygame.sprite.Sprite):
    def __init__(self, pos, size):
        super().__init__()
        self.pos = pos
        self.image = pygame.image.load('assets/end_gem.png')
        self.rect = self.image.get_rect()
        self.rect.topleft = pos

    def update(self, x_Shift):
        self.rect.x += x_Shift
