#c
from typing import Literal

import pygame

C_BLUE = (22, 0, 221)
C_WHITE = (255, 255, 255)
C_YELLOW = (255, 255, 0)
C_GREEN = (0, 128, 0)
C_CYAN = (0, 128, 128)
C_BLACK = (0, 0, 0)


#E
EVENT_ENEMY = pygame.USEREVENT + 1

EVENT_TIMEOUT = pygame.USEREVENT + 2

ENTITY_SPEED = {
    'Level1Bg0': 0,
    'Level2Bg0': 0,
    'Level3Bg0': 0,
    'Level4Bg0': 0,
    'Level5Bg0': 0,
    'Level6Bg0': 0,
    'Level7Bg0': 0,
    'Player1': 3,
    'Player1Shot': 1,
    'Player2': 3,
    'Player2Shot': 3,
    'Enemy1': 1,
    'Enemy2': 1,
    'Enemy3': 1,
    'Enemy4': 1,
    'Enemy5': 1,
    'Enemy6': 1,
    'Enemy7': 1,
    'Enemy1Shot': 5,
    'Enemy2Shot': 2,
    'Enemy3Shot': 2,
    'Enemy4Shot': 2,
    'Enemy5Shot': 2,
    'Enemy6Shot': 2,
    'Enemy7Shot': 15,
}

ENTITY_DAMAGE = {
    'Level1Bg0': 0,
    'Level2Bg0': 0,
    'Level3Bg0': 0,
    'Level4Bg0': 0,
    'Level5Bg0': 0,
    'Level6Bg0': 0,
    'Level7Bg0': 0,
    'Player1': 1,
    'Player1Shot': 25,
    'Player2': 1,
    'Player2Shot': 20,
    'Enemy1': 1,
    'Enemy2': 1,
    'Enemy3': 1,
    'Enemy4': 1,
    'Enemy5': 1,
    'Enemy6': 1,
    'Enemy7': 1,
    'Enemy1Shot': 20,
    'Enemy2Shot': 15,
    'Enemy3Shot': 2,
    'Enemy4Shot': 2,
    'Enemy5Shot': 2,
    'Enemy6Shot': 2,
    'Enemy7Shot': 50,
}

ENTITY_SCORE = {
    'Level1Bg0': 0,
    'Level2Bg0': 0,
    'Level3Bg0': 0,
    'Level4Bg0': 0,
    'Level5Bg0': 0,
    'Level6Bg0': 0,
    'Level7Bg0': 0,
    'Player1': 0,
    'Player1Shot': 0,
    'Player2': 0,
    'Player2Shot': 0,
    'Enemy1': 100,
    'Enemy2': 125,
    'Enemy3': 125,
    'Enemy4': 125,
    'Enemy5': 125,
    'Enemy6': 125,
    'Enemy7': 125,
    'Enemy1Shot': 0,
    'Enemy2Shot': 0,
    'Enemy3Shot': 0,
    'Enemy4Shot': 0,
    'Enemy5Shot': 0,
    'Enemy6Shot': 0,
    'Enemy7Shot': 0,
}


ENTITY_HEALTH = {
    'Level1Bg0': 999,
    'Level2Bg0': 999,
    'Level3Bg0': 999,
    'Level4Bg0': 999,
    'Level5Bg0': 999,
    'Level6Bg0': 999,
    'Level7Bg0': 999,
    'Player1': 300,
    'Player1Shot': 1,
    'Player2': 300,
    'Player2Shot': 1,
    'Enemy1': 50,
    'Enemy2': 60,
    'Enemy3': 60,
    'Enemy4': 60,
    'Enemy5': 60,
    'Enemy6': 60,
    'Enemy7': 60,
    'Enemy1Shot': 1,
    'Enemy2Shot': 1,
    'Enemy3Shot': 1,
    'Enemy4Shot': 1,
    'Enemy5Shot': 1,
    'Enemy6Shot': 1,
    'Enemy7Shot': 1,
}

ENTITY_SHOT_DELAY = {
    'Player1': 20,
    'Player2': 15,
    'Enemy1': 100,
    'Enemy2': 200,
    'Enemy3': 200,
    'Enemy4': 200,
    'Enemy5': 200,
    'Enemy6': 200,
    'Enemy7': 200,
}

#M
MENU_OPTION = ('AJUDAR (jogar)',
               'PONTUAÇÃO',
               'EXIT')


PLAYER_KEY_UP = {'Player1':pygame.K_UP,
                 'Player2':pygame.K_w}
PLAYER_KEY_DOWN = {'Player1':pygame.K_DOWN,
                 'Player2':pygame.K_s}
PLAYER_KEY_LEFT = {'Player1':pygame.K_LEFT,
                 'Player2':pygame.K_a}
PLAYER_KEY_RIGHT = {'Player1':pygame.K_RIGHT,
                 'Player2':pygame.K_d}
PLAYER_KEY_SHOOT = {'Player1':pygame.K_SPACE,
                 'Player2':pygame.K_f}

SPAWN_TIME = 500 #tempo para criar inimigo

TIMEOUT_STEP = 100
TIMEOUT_LEVEL = 2000
#w
WIN_WIDTH = 1299
WIN_HEIGHT = 735

# S
SCORE_POS = {'Title': (WIN_WIDTH / 2, 50),
             'EnterName': (WIN_WIDTH / 2, 80),
             'Label': (WIN_WIDTH / 2, 90),
             'Zoeira': (WIN_WIDTH / 2, 110),
             'Name': (WIN_WIDTH / 2, 130),
             0: (WIN_WIDTH / 2, 130),
             1: (WIN_WIDTH / 2, 150),
             2: (WIN_WIDTH / 2, 170),
             3: (WIN_WIDTH / 2, 190),
             4: (WIN_WIDTH / 2, 210),
             5: (WIN_WIDTH / 2, 230),
             6: (WIN_WIDTH / 2, 250),
             7: (WIN_WIDTH / 2, 270),
             8: (WIN_WIDTH / 2, 290),
             9: (WIN_WIDTH / 2, 310),
             }