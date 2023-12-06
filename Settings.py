import pygame

level_map1 = [
'                                                                                                            ',
'                                                                                                            ',
'                                                                                                            ',
' UI                             X                                                                      ',
' LRP                               X                                  X                                  ',
' LXFIE                     UFFI                                                                           ',
'UXXXXFI     UFFFI        UFXXXXFFFFFFFFI                  XXX       XXX                                 ',
'LXXXXXXFFFFFFXXXXXFI   UFFXXFFFFFFFXXXXXXFFFFFFFFFFFFFFFFFFFXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
'LXXXXXXXX  XXXXXXXXXI  LXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
'LXXXXXXXXXXXXXXXXXXXXFFXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
'LXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX']

level_map2 = [
'                                                                                                            ',
'                                                                                                            ',
'                                                                                                            ',
' UI        XXXXXXXXXXX                      X                                                                      ',
' LRP                               X                                  X                                  ',
' LXFIE                     UFFI                                                                           ',
'UXXXXFI      UFFFI        UFXXXXFFFFFFFFI       E           XXX       XXX                                 ',
'LXXXXXXFFFFFFXXXXXFI   UFFXXFFFFFFFXXXXXXFFFFFFFFFFFFFFFFFFFXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
'LXXXXXXXX  XXXXXXXXXI  LXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
'LXXXXXXXXXXXXXXXXXXXXFFXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
'LXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX']


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