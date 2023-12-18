import pygame
from utils import utils

class Bandit(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.animations = {'run': []}
        self.import_character_assets()
        self.frame_i = 0
        self.animation_speed = 0.15
        self.image = self.animations['run'][self.frame_i]
        self.rect = self.image.get_rect()
        self.rect.topleft = pos
        self.speed = 1
        self.state = 'run'

        self.right_state = True

        self.gravity = 0.5
        self.direction = pygame.math.Vector2(0,0)

    def apply_gravity(self):
        self.direction.y += self.gravity
        self.rect.y += self.direction.y

    def move_enemy(self):
        if self.right_state:
            self.direction.x = 5
        else:
            self.direction.x = -5

    def rotate_direction(self):
        if self.right_state:
            self.right_state = False
        else:
            self.right_state = True

    def import_character_assets(self):
        character_path = 'assets/enemy/'

        for animation in self.animations.keys():
            full_path = character_path + animation
            self.animations[animation] = utils.import_folder(full_path)

    def animate_enemy(self):
        animation = self.animations[self.state]

        self.frame_i += self.animation_speed
        if self.frame_i > len(animation):
            self.frame_i = 0

        image = animation[int(self.frame_i)]

        if self.right_state:
            flipped = pygame.transform.flip(image, True, False)
            self.image = flipped

        else:
            self.image = image



    def update(self, x_Shift):
        self.rect.x += x_Shift
        self.animate_enemy()