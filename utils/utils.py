import pygame

def loadTexture(textureName):
    img = pygame.image.load('assets/' + textureName)
    return img