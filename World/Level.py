import pygame
from Settings import *
from World import Platform
from entities.PlayerEntity import Player
from entities.AngryEntity import Bandit
from tiles import Tiles
from tiles import *
from World.EnemyFrame import *
from utils.manageLevelAcess import *

class Level:
    def __init__(self, level_data, surface, level_num):
        self.display_surface = surface
        self.setup_level(level_data)
        self.level_num = level_num

        self.world_shift = 0


    def setup_level(self,layout):
        self.enemy_frame = pygame.sprite.Group()
        self.enemy = pygame.sprite.Group()
        self.tiles = pygame.sprite.Group()
        self.player = pygame.sprite.GroupSingle()


        self.enemy_count = 0
        self.won_lvl = False

        for row_index, row in enumerate(layout):
            for column_index, cell in enumerate(row):
                print(f'{row_index}{column_index}:{cell}')

                x = column_index * tile_size
                y = row_index * tile_size
                if cell == "G":
                    frame = EnemyFrame((x,y), tile_size)
                    self.enemy_frame.add(frame)

                if cell == "F":
                    underground = Tiles((x,y), tile_size)
                    self.tiles.add(underground)

                if cell == 'L':
                    vertical = TileGroundVerticalLeft((x,y), tile_size)
                    self.tiles.add(vertical)

                if cell == 'R':
                    vertical = TileGroundVerticalRight((x,y), tile_size)
                    self.tiles.add(vertical)

                if cell == 'U':
                    vertical = TileGroundVerticalLeftUp((x,y), tile_size)
                    self.tiles.add(vertical)

                if cell == 'I':
                    vertical = TileGroundVerticalRightUp((x,y), tile_size)
                    self.tiles.add(vertical)

                if cell == 'E':
                    enemy_sprite = Bandit((x, y))
                    self.enemy.add(enemy_sprite)
                    self.enemy_count += 1
                if cell == 'X':
                    tile = TileUnderground((x,y), tile_size)
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
                if enemy.rect.colliderect(player.rect):
                    if not player.damage_cd:
                        player.health = player.health - 1
                        player.direction.x -= 15
                        player.damage_cd = True

                    else:
                        pygame.time.set_timer(pygame.USEREVENT, 20)

                        for e in pygame.event.get():
                            if e.type == pygame.USEREVENT:
                                player.damage_cd = False

                if sprite.rect.colliderect(enemy.rect):
                    enemy.rotate_direction()
                    if enemy.direction.x < 0:
                        enemy.rect.left = sprite.rect.right
                    if enemy.direction.x > 0:
                        enemy.rect.right = sprite.rect.left

                for frame in self.enemy_frame.sprites():
                    if enemy.rect.colliderect(frame.rect):
                        enemy.rotate_direction()

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

                            enemy.direction.y = 0
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

    def check_enemy_collision(self):
        enemy_collision = pygame.sprite.spritecollide(self.player.sprite, self.enemy, False)

        if enemy_collision:
            for enemy in enemy_collision:
                enemy_center = enemy.rect.centery
                enemy_top = enemy.rect.top

                player_bottom = self.player.sprite.rect.bottom

                if enemy_top < player_bottom < enemy_center and self.player.sprite.direction.y >= 0:
                    self.player.sprite.direction.y = -15
                    enemy.kill()
                    self.enemy_count -= 1

                    if self.enemy_count <= 0:
                        if get_level('assets/data.txt') < self.level_num:
                            write_completed_lvl('assets/data.txt')
                        self.won_lvl = True

    def run(self):
        hp = self.player.sprite.health
        x = 10
        y = 10

        for i in range(hp):
            x += 50
            self.display_surface.blit(pygame.image.load('assets/heart.png'), (x,y))

        for e in self.enemy:
            e.move_enemy()

        self.tiles.update(self.world_shift)
        self.tiles.draw(self.display_surface)
        self.enemy_frame.update(self.world_shift)
        self.enemy_frame.draw(self.display_surface)
        self.scroll_x()
        self.player.update()
        self.enemy.update(self.world_shift)
        self.enemy.draw(self.display_surface)
        self.horizontal_movement_collide()
        self.vertical_movement_collide()
        self.player.draw(self.display_surface)
        self.check_enemy_collision()

        if self.player.sprite.health <= 0:
            self.player.sprite.out_of_hp(self.display_surface)

        if self.won_lvl:
            self.display_surface.blit(pygame.image.load('assets/win.png'), (0, 0))
