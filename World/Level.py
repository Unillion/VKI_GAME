import pygame
from Settings import *
from World import Platform
from entities.PlayerEntity import Player
from entities.AngryEntity import Bandit
from tiles import Tiles
from tiles import TileUnderground

class Level:
    def __init__(self, level_data, surface):
        self.display_surface = surface
        self.setup_level(level_data)

        self.world_shift = 0

    def setup_level(self,layout):
        self.enemy = pygame.sprite.Group()
        self.tiles = pygame.sprite.Group()
        self.player = pygame.sprite.GroupSingle()


        for row_index, row in enumerate(layout):
            for column_index, cell in enumerate(row):
                print(f'{row_index}{column_index}:{cell}')

                x = column_index * tile_size
                y = row_index * tile_size
                if cell == "F":
                    underground = TileUnderground((x,y), tile_size)
                    self.tiles.add(underground)

                if cell == 'E':
                    enemy_sprite = Bandit((x, y))
                    self.enemy.add(enemy_sprite)
                if cell == 'X':
                    tile = Tiles((x,y), tile_size)
                    self.tiles.add(tile)
                if cell == 'P':
                    player_sprite = Player((x,y))
                    self.player.add(player_sprite)


    def scroll_x(self):
        player = self.player.sprite
        player_x = player.rect.centerx
        direction_x = player.direction.x
        if player_x < W / 4 and direction_x < 0:
            self.world_shift = 5
            player.speed = 0
        elif player_x > W - (W/4) and direction_x > 0:
            self.world_shift = -5
            player.speed = 0
        else:
            self.world_shift = 0
            player.speed = 1

    def horizontal_movement_collide(self):
        player = self.player.sprite
        enemies = self.enemy.sprites()

        for enemy in enemies:
            enemy.rect.x += enemy.direction.x * enemy.speed
            for sprite in self.tiles.sprites():
                for enemy in enemies:
                    if sprite.rect.colliderect(enemy.rect):
                        if enemy.direction.x < 0:
                            enemy.rect.left = sprite.rect.right
                        if enemy.direction.x > 0:
                            enemy.rect.right = sprite.rect.left

        player.rect.x += player.direction.x * player.speed

        for sprite in self.tiles.sprites():

            if sprite.rect.colliderect(player.rect):
                if player.direction.x < 0:
                    player.rect.left = sprite.rect.right
                elif player.direction.x > 0:
                    player.rect.right = sprite.rect.left

    def vertical_movement_collide(self):
        player = self.player.sprite
        enemies = self.enemy.sprites()

        for enemy in enemies:
            enemy.apply_gravity()
            for sprite in self.tiles.sprites():
                for enemy in enemies:
                    if sprite.rect.colliderect(enemy.rect):
                        if enemy.direction.y > 0:
                            enemy.rect.bottom = sprite.rect.top

                        if enemy.direction.y < 0:
                            enemy.rect.top = sprite.rect.bottom
        player.apply_gravity()

        for sprite in self.tiles.sprites():

            if sprite.rect.colliderect(player.rect):
                if player.direction.y > 0:
                    player.direction.y = 0
                    player.rect.bottom = sprite.rect.top

                    player.isJumped = player.isJumped = False
                elif player.direction.y < 0:
                    player.rect.top = sprite.rect.bottom

    def run(self):

        self.tiles.update(self.world_shift)
        self.tiles.draw(self.display_surface)
        self.scroll_x()
        self.player.update()
        self.enemy.update(self.world_shift)
        self.enemy.draw(self.display_surface)
        self.horizontal_movement_collide()
        self.vertical_movement_collide()
        self.player.draw(self.display_surface)