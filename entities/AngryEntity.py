import pygame

class Bandit(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.image = pygame.Surface((32, 64))
        self.image.fill('red')
        self.rect = self.image.get_rect()
        self.rect.topleft = pos
        self.speed = 1

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



    def update(self, x_Shift):
        self.rect.x += x_Shift