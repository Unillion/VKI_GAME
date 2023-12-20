import pygame

'''
F - тропинка
U - слева-вверз
L - вверх
I - слева-вниз
P - игрок
E - враг
G - отталкиватель-врагов
x - подземный блок

'''
level_map1 = [
'BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB',
'B                                                                                                          B',
'B      G  E   G                                                                                            B',
'B       UFFFFI  G      E        G                                                                          B',
'B                UFFFFFFFFFFFFFI         G     E    G                                                      B',
'B                               G  E   G  UFFFFFFFFI                 G     E       G                       B',
'B                                UFFFFI               G   E      E  G UFFFFFFFFFFFI                        B',
'B       G  E                          G                UFFFFFFFFFFFI                                       B',
'B     P  UFFFFFFFFFFFFFFFFFFFFFFFFFFFI                                                                     B',
'UFFFFFFFFXXXXXXXXXXXXXXXXXXXXXXXXXXXXXFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF',
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

level_map3 = [
'                                                                                                            ',
'                                                                                                            ',
'                                                                                                            ',
' UI        XXXXXXXXXXX                      X                                                                      ',
' LRP                               X                                  X                                  ',
' LXFIE                     UFFI                                                                           ',
'UXXXXFI      UFFFI        UFXXXXFFFFFFFFI                  XXX       XXX                                 ',
'LXXXXXXFFFFFFXXXXXFI   UFFXXFFFFFFFXXXXXXFFFFFFFFFFFFFFFFFFFXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
'LXXXXXXXX  XXXXXXXXXI  LXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
'LXXXXXXXXXXXXXXXXXXXXFFXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
'LXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX']

level_map4 = [
'                                                                                                            ',
'                                                                                                            ',
'                                                                                                            ',
' UI        XXXXXXXXXXX                      X                                                                      ',
' LRP                               X                                  X                                  ',
' LXFIE  V                 UFFI                                                                          ',
'UXXXXFI      UFFFI        UFXXXXFFFFFFFFI       E          XXX       XXX                                 ',
'LXXXXXXFFFFFFXXXXXFI   UFFXXFFFFFFFXXXXXXFFFFFFFFFFFFFFFFFFFXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
'LXXXXXXXX  XXXXXXXXXI  LXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
'LXXXXXXXXXXXXXXXXXXXXFFXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
'LXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX']


levels = [level_map1, level_map2, level_map3, level_map4]

def getLevel(index):
    return levels[index]

tile_map = set()
tile_size = 64

W = 1200
H = len(level_map1) * tile_size
print(H)



WHITE = (0,0,0)
BLUE = (0, 70, 225)