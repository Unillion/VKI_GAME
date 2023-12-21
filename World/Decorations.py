import pygame
from utils.utils import *

pygame.init()


class Arrow(pygame.sprite.Sprite):
    def __init__(self, pos, size, isRight):
        super().__init__()
        self.image = pygame.Surface((size, size))
        self.image.fill('blue')
        if isRight:
            self.image = pygame.image.load('assets/decorations/arrow.png')
        else:
            self.image = pygame.transform.flip(pygame.image.load('assets/decorations/arrow.png'), True, False)
        self.rect = self.image.get_rect()
        self.rect.topleft = pos

    def update(self, x_Shift):
        self.rect.x += x_Shift

class Fence(pygame.sprite.Sprite):
    def __init__(self, pos, size):
        super().__init__()
        self.image = pygame.Surface((size, size))
        self.image.fill('blue')
        self.image = pygame.image.load('assets/decorations/fence.png')
        self.rect = self.image.get_rect()
        self.rect.topleft = pos

    def update(self, x_Shift):
        self.rect.x += x_Shift

class Leaves(pygame.sprite.Sprite):
    def __init__(self, pos, size):
        super().__init__()
        self.animations = {'idle':[]}

        self.load_animation()
        self.frame_i = 0
        self.animation_speed = 0.15
        self.image = pygame.Surface((size, size))
        self.image.fill('blue')
        self.image = pygame.image.load('assets/decorations/fence.png')
        self.rect = self.image.get_rect()
        self.rect.topleft = pos

    def load_animation(self):
        path = 'assets/decorations/leaves/'

        self.animations['idle'] = import_folder(path)

    def animate(self):
        animation = self.animations['idle']
        self.frame_i += self.animation_speed
        if self.frame_i > len(animation):
            self.frame_i = 0

        image = animation[int(self.frame_i)]
        self.image = image

    def update(self, x_Shift):
        self.animate()
        self.rect.x += x_Shift