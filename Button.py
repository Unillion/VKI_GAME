import pygame
class Buttons():
    def __init__(self, x,y, screen, image):
        self.screen = screen
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)

    def draw(self):
        self.screen.blit(self.image, (self.rect.x, self.rect.y))


