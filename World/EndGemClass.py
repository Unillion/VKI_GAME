import pygame
import random
from utils.utils import *

pygame.init()


class EndGem(pygame.sprite.Sprite):
    def __init__(self, pos, size):
        super().__init__()
        self.pos = pos
        self.animations = {'idle': []}
        self.import_character_assets()
        self.frame_i = 0
        self.animation_speed = 0.15
        self.image = self.animations['idle'][self.frame_i]
        self.rect = self.image.get_rect()
        self.rect.topleft = pos
        self.y = 0
        self.up = True

    def import_character_assets(self):
        path = 'assets/decorations/gem/'
        self.animations['idle'] = import_folder(path)

    def animate(self, screen):
        yCap = 10
        yMin = 0

        if self.up:
            self.rect.y -= 1
            self.y += 1
            print(self.y)
            if self.y >= yCap:
                self.up = False
        else:
            self.rect.y += 1
            self.y -= 1
            if self.y <= yMin:
                self.up = True

        animation = self.animations['idle']
        self.frame_i += self.animation_speed
        if self.frame_i > len(animation):
            self.frame_i = 0

        image = animation[int(self.frame_i)]
        self.image = pygame.transform.scale(image, (64,64))

    def update(self, x_Shift, screen):

        self.animate(screen)
        self.rect.x += x_Shift
