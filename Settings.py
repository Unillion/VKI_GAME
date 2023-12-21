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
1/2- стрелка вправо влево
3 - заборчик

'''
level_map1 = [
'B                                                                                                          B',
'B                                                                                                          B',
'B      G  E3  G                                                                                            B',
'B       UFFFFI  G   23 E  3     G                                                                          B',
'B        6  6    UFFFFFFFFFFFFFI          G     E 1 G                                                      B',
'B                   6     6     G  E21 G  UFFFFFFFFI                 G     E       G                       B',
'B                                UFFFFI      6  6     G   E  1   E  G UFFFFFFFFFFFI                        B',
'B       G  E 1  3                     G                UFFFFFFFFFFFI       6    6                          B',
'B     P  UFFFFFFFFFFFFFFFFFFFFFFFFFFFI             3                                                       B',
'UFFFFFFFFXXXXXXXXXXXXXXXXXXXXXXXXXXXXXFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF',
'LXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX']

level_map2 = [
'BBB                                                                                                  BBBBBBB',
'B                   G    E 3  G                                                                            B',
'B                    UFFFFFFFI                G 3  E    G           G    E  3  G                           B',
'B                     6 6  6                   UFFFFFFFI             UFFFFFFFFI                            B',
'B                                              6     6               6   6   6                             B',
'B                                    251                    1                    1  G       E    3   G     B',
'B                          31    UFFFFFFFFFIG3  E  3  GUFFFFFFFFFFFFIG   E   GUFFFFFFFFFFFFFFFFFFFFFFFFFFFFB',
'B       G  1   E  3     GUFFFFFFFXXXXXXXXXXXFFFFFFFFFFFXXXXXXXXXXXXXXFFFFFFFFFXXXXXXXXXXXXXXXXXXXXXXXXXXXXXB',
'B     P  UFFFFFFFFFFFFFFFXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXB',
'UFFFFFFFFXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
'LXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX']

level_map3 = [
'BBB                                                                                                  BBBBBBB',
'B                                                                     G     E  1 G                         B',
'B                                  G     E    G                        UFFFFFFFFI                          B',
'B              G      7    E 1 G    UFFFFFFFFI                               6                        GE3 GB',
'B               UFFFF888FFFFFFI      6                                                                UFFFFF',
'B                  6        6     2 3  7  31                  51              1   G    3  E   7  E 3 UXXXXXX',
'B 31 P                            UFFFF888FFIG3   E    GUFFFFFFFFFFFFIG  77E  GUFFFFFFFFFFFFF88888FFFFFFFFFFF',
'FFFFI       1  7G   3 E GUFFFFFFFXXXXXXXXXXXXFFFFFFFFFXXXXXXXXXXXXXXX888888888XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
'XXXXXI 3  UFFF888FFFFFFFFXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
'XXXXXXFFFFXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX']

level_map4 = [
'BBB                                                                                                  BBBBBBB',
'B                                                                                                          B',
'B                                                V                  G   E 3    G                           B',
'B            G        G                          8                   UFFFFFFFFI                            B',
'B      P      UFFFFFFI                           X                      6     6                            B',
'B     UFFI     6    6                            X            52               3 G         E   3    GUXXXXXX',
'B 5                    21  G   3    E       G1 5 X 52  GUFFFFFFFFFFFFIG    E  GUFFFFFFFFFFFFFFFFFFFFFXXXXXXX',
'FFFFIG   E  3     3 E GUFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFXXXXXXXXXXXXXXFFFFFFFFFXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
'XXXXXFFFFFFFFFFFFFFFFFFXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX']


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