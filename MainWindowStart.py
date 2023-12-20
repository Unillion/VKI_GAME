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
from pygame import mixer

pygame.init()

screen = pygame.display.set_mode((W, H), pygame.RESIZABLE)

bg = pygame.image.load('assets/menu_background.png')
bg = pygame.transform.scale(bg, (W, H))

pygame.display.set_icon(pygame.image.load('assets/gameicon.png'))
pygame.display.set_caption("The Dawn Of New World")

clock = pygame.time.Clock()

start_button = Buttons(100, 150, screen, pygame.image.load('assets/start_btn.png'))
file_help = Buttons(100, 300, screen, pygame.image.load('assets/help_btn.png'))
quit_button = Buttons(100, 450, screen, pygame.image.load('assets/quit_btn.png'))
quit_from_help = Buttons(W/2 - 100, 570, screen, pygame.image.load('assets/quit_btn.png'))

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
                    pygame.display.update()

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
                                level1 = Level(level_map1, screen, 1, menu, win)

                            if buttons_of_levels.index(button) == 1 and get_level('assets/data.txt') >= 1:
                                menu = False
                                level_choosing = False
                                LevelTwo = True
                                level2 = Level(level_map2, screen, 2, menu, win)

                            if buttons_of_levels.index(button) == 2 and get_level('assets/data.txt') >= 2:
                                menu = False
                                level_choosing = False
                                LevelThree = True
                                level3 = Level(level_map3, screen, 3, menu, win)
                            if buttons_of_levels.index(button) == 3 and get_level('assets/data.txt') >= 3:
                                menu = False
                                level_choosing = False
                                LevelFour = True
                                level4 = Level(level_map4, screen, 4, menu, win)
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
            drawMenu(screen, buttons_of_levels)

        elif helping:
            screen.blit(utils.utils.loadTexture('help_file_for_popov.jpg'), (0, 0))
            quit_from_help.draw()
            pygame.display.update()
        else:
            alpha = alpha - 2
            start_button.draw()
            quit_button.draw()
            file_help.draw()
            fade(screen, alpha)

            pygame.mouse.set_visible(True)
            screen.blit(bg, (0, 0))


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
            screen.blit(pygame.image.load('assets/win.png'), (0, 0))

        pygame.display.update()
