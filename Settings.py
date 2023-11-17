import pygame

level_map1 = [
'                                                                                                            ',
'                                                                                                            ',
'                                                                                                            ',
' XX        XX                      X                                                                      ',
' XXP                               X                                  X                                  ',
' XXXXE       E              XXXX                                                                           ',
'XXXXXXX      XXXXX        XXXXXXXXXXXXXXXXX       E           XXX       XXX                                 ',
'XXXXXXXXXXXXXXXXXXXX   XXXXXFFFFFFFXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
'XXXXXXXXX  XXXXXXXXXX  XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX']

level_map2 = ['                                                   X',
'                                                                 X',
'                                                                 X',
' XX        XX               XX       X                           X',
' XX         XX               E       X                          X',
' XXXX          E           XXXXXP                                X',
'XXXXXXX      XXXXX        XXXXXXXXXXXXXXXXX       E           XXX',
'XXXXXXXXXXXXXXXXXXXX   XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
'XXXXXXXXX  XXXXXXXXXX  XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
'EEEEEEEEEEEEEEEEEEXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX']

levels = [level_map1, level_map2]

def getLevel(index):
    return levels[index]

tile_map = set()
tile_size = 64

W = 1200
H = len(level_map1) * tile_size
print(H)



WHITE = (0,0,0)
BLUE = (0, 70, 225)