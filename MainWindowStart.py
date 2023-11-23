from Settings import *
from Button import Buttons
import sys
import pygame
from ScreenGame.GameField import *
from World.Level import Level
from ScreenGame.LevelChooseMenu.LvlChose import *
from ScreenGame.GameField import fade
from ScreenGame.PauseMenu import drawPause
from pygame import mixer

pygame.init()

screen = pygame.display.set_mode((W, H), pygame.RESIZABLE)

bg = pygame.image.load('assets/menu_background.png')
bg = pygame.transform.scale(bg, (W, H))

pygame.display.set_icon(pygame.image.load('assets/gameicon.png'))
pygame.display.set_caption("The Dawn Of New World")

clock = pygame.time.Clock()

start_button = Buttons(100, 200, screen, pygame.image.load('assets/start_btn.png'))
quit_button = Buttons(100, 400, screen, pygame.image.load('assets/quit_btn.png'))
exit_ingame_button = Buttons(400, 400, screen, pygame.image.load('assets/quit_btn.png'))
alpha = 255
LevelOne = False
LevelTwo = False

# 0 - 1 lvl
# 1 - 2 lvl
# 2 - 3 lvl
# 3 = 4 lvl

running = True

menu = True
esc = False
level_choosing = False

buttons_of_levels = createButtonList(screen, images)

while running:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                if not menu:
                    if not esc:
                        esc = True
                    else:
                        esc = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse = pygame.mouse.get_pos()

            if pygame.mouse.get_pressed()[0]:
                if esc:
                    if exit_ingame_button.rect.collidepoint(mouse):
                        if LevelOne:
                            LevelOne = False
                        elif LevelTwo:
                            LevelTwo = False
                        esc = False
                        menu = True


                if menu and not esc:
                    if level_choosing:
                        for button in buttons_of_levels:
                            if button.rect.collidepoint(mouse):
                                if buttons_of_levels.index(button) == 0:
                                    menu = False
                                    level_choosing = False
                                    LevelOne = True
                                    level1 = Level(level_map1, screen)

                                if buttons_of_levels.index(button) == 1:
                                    menu = False
                                    level_choosing = False
                                    LevelTwo = True
                                    level2 = Level(level_map2, screen)

                                if buttons_of_levels.index(button) == 2:
                                    level_choosing = False
                                if buttons_of_levels.index(button) == 3:
                                    level_choosing = False
                    else:
                        if start_button.rect.collidepoint(mouse):
                            level_choosing = True
                        elif quit_button.rect.collidepoint(mouse):
                            pygame.quit()
                            sys.exit()
    if menu:
        if not esc:
            if level_choosing:
                drawMenu(screen, buttons_of_levels)

            else:
                alpha = alpha - 2
                start_button.draw()
                quit_button.draw()
                fade(screen, alpha)

                pygame.mouse.set_visible(True)
                screen.blit(bg, (0, 0))

    else:
        if esc:
            pygame.mouse.set_visible(True)
            drawPause(screen, exit_ingame_button)

        else:
            if not level_choosing:
                screen.fill(WHITE)
                pygame.mouse.set_visible(False)

                if LevelOne:
                    level1.run()
                elif LevelTwo:
                    level2.run()

                pygame.display.update()


