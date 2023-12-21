import pygame.sprite
from utils.utils import *


class JumpPad(pygame.sprite.Sprite):
    def __init__(self, pos, size):
        super().__init__()
        self.animations = {'use': []}
        self.load_texture()
        self.frame_i = 0
        self.animation_speed = 1
        self.image = pygame.Surface((size,size))
        self.image = self.animations['use'][self.frame_i]
        self.rect = self.image.get_rect()
        self.rect.topleft = pos

    def load_texture(self):
        path = 'assets/interactionable/jump_pad/'

        self.animations['use'] = import_folder(path)

    def animate(self):
        animation = self.animations['use']

        self.frame_i += self.animation_speed
        if self.frame_i > len(animation):
            self.frame_i = 0

        image = animation[int(self.frame_i)]
        self.image = image


    def update(self, x_Shift):
        self.rect.x += x_Shift


class FireBlock(pygame.sprite.Sprite):
    def __init__(self, pos, size):
        super().__init__()
        self.animations = {'idle': []}
        self.load_texture()
        self.frame_i = 0
        self.animation_speed = 0.15
        self.image = pygame.Surface((size, size))
        self.image = self.animations['idle'][self.frame_i]
        self.rect = self.image.get_rect()
        self.rect.topleft = pos

    def load_texture(self):
        path = 'assets/interactionable/fire/'

        self.animations['idle'] = import_folder(path)

    def animate(self):
        animation = self.animations['idle']

        self.frame_i += self.animation_speed
        if self.frame_i > len(animation):
            self.frame_i = 0

        image = animation[int(self.frame_i)]
        self.image = pygame.transform.scale(image, (128,64))

    def update(self, x_Shift):
        self.animate()
        self.rect.x += x_Shift

class Ladder(pygame.sprite.Sprite):
    def __init__(self, pos, size):
        super().__init__()
        self.image = pygame.Surface((size,size))
        self.image = pygame.image.load('assets/interactionable/ladder.png')
        self.rect = self.image.get_rect()
        self.rect.topleft = pos

    def update(self, x_Shift):
        self.rect.x += x_Shift


