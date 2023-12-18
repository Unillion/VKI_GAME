import pygame
from Settings import *
from World import Platform
from entities.PlayerEntity import Player
from entities.AngryEntity import Bandit
from tiles import Tiles
from tiles import *
from World.EnemyFrame import *
from utils.manageLevelAcess import *
from World.EndGemClass import *
from World import Particle

class Level:
    def __init__(self, level_data, surface, level_num, menu, win):
        self.display_surface = surface
        self.setup_level(level_data)
        self.level_num = level_num
        self.menu = menu
        self.win = win
        self.x = 0

        self.world_shift = 0
        self.particle = pygame.sprite.GroupSingle()

        self.player_on_ground = True


    def render_jump_particle(self, pos):
        jump_particle = Particle.ParticleEffect(pos, 'jump')
        self.particle.add(jump_particle)

    def create_landing_dust(self):
        #if not self.player_on_ground and self.player.sprite.ground and self.particle.sprite:
            if self.player_on_ground != self.player.sprite.ground or self.player.sprite.celling:
                if self.player.sprite.groups():

                    if self.player.sprite.right:
                        offset = pygame.math.Vector2(10, 15)
                    else:
                        offset = pygame.math.Vector2(-10, 15)
                    fall_dust_particle = Particle.ParticleEffect(self.player.sprite.rect.midbottom - offset, 'land')
                    self.particle.add(fall_dust_particle)

    def setup_level(self,layout):
        self.enemy_frame = pygame.sprite.Group()
        self.enemy = pygame.sprite.Group()
        self.tiles = pygame.sprite.Group()
        self.player = pygame.sprite.GroupSingle()
        self.gems = pygame.sprite.Group()


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
                    player_sprite = Player((x,y), self.display_surface, self.render_jump_particle)
                    self.player.add(player_sprite)
                if cell == "V":
                    gem = EndGem((x,y), tile_size)
                    self.gems.add(gem)

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


    def horizontal_movement_collide(self, menu):
        player = self.player.sprite
        enemies = self.enemy.sprites()
        gems = self.gems.sprites()


        for enemy in enemies:
            enemy.rect.x += enemy.direction.x * enemy.speed
            for sprite in self.tiles.sprites():
                if self.level_num == 4:
                    for gem in gems:
                        if player.rect.colliderect(gem.rect) and self.enemy_count == 0:
                            self.win = True
                            print('game over')

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
                        player.left = True
                        self.x = player.rect.left
                    elif player.direction.x > 0:
                        player.rect.right = sprite.rect.left
                        player.right = True
                        self.x = player.rect.right

        if player.left and (player.rect.left < self.x or player.direction.x >= 0):
            player.left = False
        if player.right and (player.rect.right > self.x or player.direction.x <= 0):
            player.right = False
        return menu


    def vertical_movement_collide(self):
        player = self.player.sprite
        enemies = self.enemy.sprites()
        self.player_on_ground = player.ground

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
                    player.ground = True


                    player.isJumped = player.isJumped = False
                elif player.direction.y < 0:
                    player.rect.top = sprite.rect.bottom
                    player.celling = True

            else:
                player.celling = False
        if player.ground and player.direction.y < 0 or player.direction.y > 1:
            player.ground = False
        if player.celling and player.direction.y > 0.1:
            player.celling = False


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
                            if get_level('assets/data.txt') != 3:
                                write_completed_lvl('assets/data.txt')
                        self.won_lvl = True

    def draw_bg(self, screen):
        if self.level_num == 1:
            screen.blit(pygame.image.load('assets/menu_background.png'), (0,0))

    def run(self):
        self.draw_bg(self.display_surface)

        hp = self.player.sprite.health
        x = 10
        y = 10



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
        self.horizontal_movement_collide(self.menu)
        self.vertical_movement_collide()
        self.player.draw(self.display_surface)
        #self.get_player_on_ground()
        self.create_landing_dust()
        self.check_enemy_collision()
        self.gems.update(self.world_shift)
        self.gems.draw(self.display_surface)
        self.particle.update(self.world_shift)
        self.particle.draw(self.display_surface)

        if self.player.sprite.health <= 0:
            self.player.sprite.out_of_hp(self.display_surface)
        for i in range(hp):
            x += 50
            self.display_surface.blit(pygame.image.load('assets/heart.png'), (x,y))
        if self.won_lvl:
            self.display_surface.blit(pygame.image.load('assets/win.png'), (0, 0))
        return self.win