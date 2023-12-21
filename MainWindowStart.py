import utils.utils
from Settings import *
from Button import Buttons
import sys
import pygame
from ScreenGame.GameField import *
from World.Level import Level
from ScreenGame.LevelChooseMenu.LvlChose import *
from ScreenGame.GameField import fade
from ScreenGame.PauseMenu import drawPause
from utils.manageLevelAcess import *
from utils.utils import *
from pygame import mixer

pygame.init()
def render_menu(screen):
    font = pygame.font.Font('assets/fonts/papyrus.ttf', 70)
    text_game_name = font.render("The Pirate Bay!", True, 'white')

    screen.blit(text_game_name, (560, 75))

def render_game_completed(screen):
    egg = pygame.transform.scale(loadTexture('danil_egg.png'), (128,128))
    surface = pygame.Surface((1800, 1200))
    surface.fill('black')
    font = pygame.font.Font('assets/fonts/papyrus.ttf', 100)
    text_level_completed = font.render("Game Completed!", True, 'yellow')
    text_quit_to_menu = font.render("Press ESC to quit to the Menu", True, 'yellow')

    screen.blit(surface, (0, 0))
    screen.blit(egg, (550, 50))
    screen.blit(text_level_completed, (300, 200))
    screen.blit(text_quit_to_menu, (20, 400))

screen = pygame.display.set_mode((W, H), pygame.FULLSCREEN | pygame.DOUBLEBUF)

label = pygame.transform.scale(loadTexture('lable.png'), (564,128))

bg = pygame.image.load('assets/backgrounds/menu_background.jpg')
bg = pygame.transform.scale(bg, (W + 80, H + 10))
bg2 = pygame.image.load('assets/backgrounds/level_level_background.jpg')
bg2 = pygame.transform.scale(bg, (W + 80, H + 10))

pygame.display.set_icon(pygame.image.load('assets/gameicon.png'))
pygame.display.set_caption("The Dawn Of New World")

clock = pygame.time.Clock()

start_button = Buttons(100, 150, screen, pygame.image.load('assets/start_btn.png'))
file_help = Buttons(100, 300, screen, pygame.image.load('assets/help_btn.png'))
quit_button = Buttons(100, 450, screen, pygame.image.load('assets/quit_btn.png'))
quit_from_help = Buttons(W/2 + 250, 570, screen, pygame.image.load('assets/quit_btn.png'))
help = pygame.transform.scale(utils.utils.loadTexture('help_file_for_popov.jpg'), (W + 20, H - 20))

alpha = 255
LevelOne = False
LevelTwo = False
LevelThree = False
LevelFour = False

# 0 - 1 lvl
# 1 - 2 lvl
# 2 - 3 lvl
# 3 = 4 lvl

running = True

menu = True
level_choosing = False
win = False
helping = False

buttons_of_levels = createButtonList(screen, images)

def disableAllLevels():
    LevelOne = False
    LevelTwo = False
    LevelThree = False
    LevelFour = False
    return LevelOne, LevelTwo, LevelThree, LevelFour


while running:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                if menu:
                    if helping:
                        LevelOne, LevelTwo, LevelThree, LevelFour = disableAllLevels()
                        menu = True
                        win = False
                else:
                    LevelOne, LevelTwo, LevelThree, LevelFour = disableAllLevels()
                    menu = True
                    win = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse = pygame.mouse.get_pos()
            if menu:
                if level_choosing:
                    for button in buttons_of_levels:
                        if button.rect.collidepoint(mouse):
                            if buttons_of_levels.index(button) == 0 and get_level('assets/data.txt') >= 0:
                                menu = False
                                level_choosing = False
                                LevelOne = True
                                level1 = Level(level_map1, screen, 1, menu)

                            if buttons_of_levels.index(button) == 1 and get_level('assets/data.txt') >= 1:
                                menu = False
                                level_choosing = False
                                LevelTwo = True
                                level2 = Level(level_map2, screen, 2, menu)

                            if buttons_of_levels.index(button) == 2 and get_level('assets/data.txt') >= 2:
                                menu = False
                                level_choosing = False
                                LevelThree = True
                                level3 = Level(level_map3, screen, 3, menu)
                            if buttons_of_levels.index(button) == 3 and get_level('assets/data.txt') >= 3:
                                menu = False
                                level_choosing = False
                                LevelFour = True
                                level4 = Level(level_map4, screen, 4, menu)
                else:
                    if helping:
                        if quit_from_help.rect.collidepoint(mouse):
                            helping = False
                    else:
                        if start_button.rect.collidepoint(mouse):
                            level_choosing = True
                        elif file_help.rect.collidepoint(mouse):
                            helping = True

                        elif quit_button.rect.collidepoint(mouse):
                            pygame.quit()
                            sys.exit()
    if menu:
        if level_choosing:
            screen.blit(bg2, (0,0))
            drawMenu(screen, buttons_of_levels)

        elif helping:
            screen.blit(pygame.transform.scale(help, (W, H)), (0, 0))
            quit_from_help.draw()
        else:
            alpha = alpha - 2
            screen.blit(bg, (0, 0))



            screen.blit(label, (500, 50))
            render_menu(screen)
            start_button.draw()
            quit_button.draw()
            file_help.draw()
            fade(screen, alpha)
            pygame.mouse.set_visible(True)


    else:
        if not level_choosing:
            pygame.mouse.set_visible(False)

            screen.fill('black')

            if LevelOne:
                level1.run()
            elif LevelTwo and get_level('assets/data.txt') >= 1:
                level2.run()
            if LevelThree and get_level('assets/data.txt') >= 2:
                level3.run()
            elif LevelFour and get_level('assets/data.txt') >= 3:
                win = level4.run()

        if win:
            render_game_completed(screen)

    pygame.display.flip()
