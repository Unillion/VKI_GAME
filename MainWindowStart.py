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


def start():
    running = True
    level = Level(level_map1, screen)

    menu = True
    esc = False
    level_choosing = False

    #mixer.music.load('assets/main_ost.mp3')
    #mixer.music.play()

    alpha = 255

    start_button = Buttons(100, 200, screen, pygame.image.load('assets/start_btn.png'))
    quit_button = Buttons(100, 400, screen, pygame.image.load('assets/quit_btn.png'))
    exit_ingame_button = Buttons(400, 400, screen, pygame.image.load('assets/quit_btn.png'))

    buttons_of_levels = createButtonList(screen, images)

    while running:
        clock.tick(60)

        print(esc)
        if menu and not esc:
            if level_choosing:
                drawMenu(screen, buttons_of_levels)
            else:
                alpha = alpha - 2
                start_button.draw()
                quit_button.draw()
                fade(screen, alpha)

                pygame.mouse.set_visible(True)
                screen.blit(bg, (0, 0))
        elif not menu and not esc and not level_choosing:

            mixer.music.stop()

            screen.fill(WHITE)
            pygame.mouse.set_visible(False)
            level.run()
            pygame.display.update()

        elif not menu and esc:
            pygame.mouse.set_visible(True)
            drawPause(screen, exit_ingame_button)

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
                            esc = False
                            menu = True
                    if menu and not esc:
                        if level_choosing:
                            for button in buttons_of_levels:
                                if button.rect.collidepoint(mouse):
                                    if buttons_of_levels.index(button) == 0:
                                        menu = False
                                        level_choosing = False
                                    if buttons_of_levels.index(button) == 1:
                                        level_choosing = False
                                    if buttons_of_levels.index(button) == 2:
                                        level_choosing = False
                                    if buttons_of_levels.index(button) == 3:
                                        level_choosing = False
                        else:
                            if start_button.rect.collidepoint(mouse):
                                print("pressed")
                                level_choosing = True
                            elif quit_button.rect.collidepoint(mouse):
                                print('quitted')
                                pygame.quit()
                                sys.exit()
