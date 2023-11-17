from Settings import *
from World.Level import *

class Player(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.image = pygame.Surface((32,64))
        self.image.fill('white')
        #self.image = pygame.image.load('assets/sprite.png')
        self.rect = self.image.get_rect()
        self.rect.topleft = pos

        #движение
        self.gravity = 0.5
        self.jump_speed = -10
        self.double_jump = 0
        self.isJumped = False
        self.speed = 100
        self.direction = pygame.math.Vector2(0,0)

    def get_input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.direction.x = -5
        elif keys[pygame.K_d]:
            self.direction.x = 5
        else:
            self.direction.x = 0

        if keys[pygame.K_SPACE]:
            self.jump()

    def apply_gravity(self):
        self.direction.y += self.gravity
        self.rect.y += self.direction.y

    def jump(self):
        print(self.double_jump)
        if self.isJumped:
            pass
        else:
            self.direction.y = self.jump_speed
            self.double_jump = self.double_jump + 1

            if self.double_jump >= 2:
                self.isJumped = True
                self.double_jump = 0


    def update(self):
        self.get_input()