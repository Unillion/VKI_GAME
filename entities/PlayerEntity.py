import pygame.transform

from Settings import *
from World.Level import *
from utils import utils
import random

class Player(pygame.sprite.Sprite):
    def __init__(self, pos, screen, render_particle):
        super().__init__()
        self.animations = {'idle': [], 'run': [], 'jump': [], 'fall': []}
        self.import_character_assets()
        self.frame_i = 0
        self.animation_speed = 0.15
        self.image = self.animations['idle'][self.frame_i]

        #self.image = pygame.Surface((32, 64))
        self.rect = self.image.get_rect()
        self.rect.topleft = pos
        self.health = 3
        self.damage_cd = False
        self.died = False

        #частицы
        self.render_particles = render_particle
        self.particle_i = 0
        self.particle_speed = 0.15
        self.screen = screen


        #движение
        self.gravity = 0.5
        self.jump_speed = -15
        self.double_jump = 0
        self.isJumped = False
        self.speed = 100
        self.direction = pygame.math.Vector2(0,0)

        #статус игрока
        self.state = 'idle'
        self.facing = True
        self.ground = False
        self.celling = False
        self.left = False
        self.right = False

    def get_input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.direction.x = -9
            self.facing = False
        elif keys[pygame.K_d]:
            self.direction.x = 9
            self.facing = True
        else:
            self.direction.x = 0

        if keys[pygame.K_SPACE]:
            if not self.isJumped:
                self.jump()
                self.render_particles(self.rect.midbottom)

    def apply_gravity(self):
        self.direction.y += self.gravity
        self.rect.y += self.direction.y

    def jump(self):
        self.direction.y = self.jump_speed
        self.isJumped = True

    def import_character_assets(self):
        character_path = 'assets/character/'

        for animation in self.animations.keys():
            full_path = character_path + animation
            self.animations[animation] = utils.import_folder(full_path)

    def out_of_hp(self, screen):
        surface = pygame.Surface((1800, 1200))
        surface.fill('black')
        font = pygame.font.Font('assets/fonts/papyrus.ttf', 100)
        text_died = font.render("You Died", True, 'red')
        text_quit_to_menu = font.render("Press ESC to quit to the Menu", True, 'red')

        screen.blit(surface, (0, 0))
        screen.blit(text_died, (450, 200))
        screen.blit(text_quit_to_menu, (20, 400))
        self.died = True

    def get_player_state(self):
        if self.direction.y < 0:
            self.state = 'jump'
        elif self.direction.y > 0:
            self.state = 'fall'
        else:
            if self.direction.x != 0:
                self.state = 'run'
            else:
                self.state = 'idle'

    def animate_player(self):
        animation = self.animations[self.state]

        self.frame_i += self.animation_speed
        if self.frame_i > len(animation):
            self.frame_i = 0

        image = animation[int(self.frame_i)]

        if self.facing:
            self.image = image
        else:
            flipped = pygame.transform.flip(image, True, False)
            self.image = flipped

        if self.ground and self.right:
            self.rect = self.image.get_rect(bottomright=self.rect.bottomright)
        elif self.ground and self.left:
            self.rect = self.image.get_rect(bottomleft=self.rect.bottomleft)
        elif self.ground:
            self.rect = self.image.get_rect(midbottom=self.rect.midbottom)
        if self.celling and self.right:
            self.rect = self.image.get_rect(topright=self.rect.topright)
        elif self.celling and self.left:
            self.rect = self.image.get_rect(topleft=self.rect.topleft)
        elif self.celling:
            self.rect = self.image.get_rect(midtop=self.rect.midtop)

    def update(self):
        if not self.died:
            self.animate_player()
            self.get_player_state()
            self.get_input()