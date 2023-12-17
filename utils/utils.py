import pygame, os
pygame.init()
screen = pygame.display.set_mode((800, 600))

def loadTexture(textureName):
    img = pygame.image.load('assets/' + textureName)
    return img

def import_folder(path):
    surface_list = []

    for _, __, img_files in os.walk(path):
        print('1')
        for image in img_files:
            full_path = path + '/' + image
            print(full_path)
            image_surf = pygame.image.load(full_path).convert_alpha()
            surface_list.append(image_surf)
    return surface_list

print(import_folder('../assets/character/idle'))