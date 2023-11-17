import pygame

class Bandit(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.hp = 5
        self.image = pygame.Surface((32, 64))
        self.image.fill('red')
        self.rect = self.image.get_rect()
        self.rect.topleft = pos

        self.speed = 100

        self.gravity = 0.5
        self.direction = pygame.math.Vector2(0,0)

    def apply_gravity(self):
        self.direction.y += self.gravity
        self.rect.y += self.direction.y

    def update(self, x_Shift):
        self.rect.x += x_Shift