import random

from code.Background import Background
from code.Const import WIN_WIDTH, WIN_HEIGHT
from code.Enemy import Enemy
from code.Player import Player


class EntityFactory:

    @staticmethod
    def get_entity(entity_name: str, position=(0, 0)):
        match entity_name:
            case 'Level1Bg':
                list_bg = []
                for i in range(1):  # NUMERO DE IMAGENS DO LEVEL
                    list_bg.append(Background(name=f'Level1Bg{i}', position=(0, 0)))
                    list_bg.append(Background(name=f'Level1Bg{i}', position=(WIN_WIDTH, 0)))
                return list_bg
            case 'Level2Bg':
                list_bg = []
                for i in range(1):
                    list_bg.append(Background(name=f'Level2Bg{i}', position=(0, 0)))
                    list_bg.append(Background(name=f'Level2Bg{i}', position=(WIN_WIDTH, 0)))
                return list_bg
            case 'Level3Bg':
                list_bg = []
                for i in range(1):
                    list_bg.append(Background(name=f'Level3Bg{i}', position=(0, 0)))
                    list_bg.append(Background(name=f'Level3Bg{i}', position=(WIN_WIDTH, 0)))
                return list_bg
            case 'Level4Bg':
                list_bg = []
                for i in range(1):
                    list_bg.append(Background(name=f'Level4Bg{i}', position=(0, 0)))
                    list_bg.append(Background(name=f'Level4Bg{i}', position=(WIN_WIDTH, 0)))
                return list_bg
            case 'Level5Bg':
                list_bg = []
                for i in range(1):
                    list_bg.append(Background(name=f'Level5Bg{i}', position=(0, 0)))
                    list_bg.append(Background(name=f'Level5Bg{i}', position=(WIN_WIDTH, 0)))
                return list_bg
            case 'Level6Bg':
                list_bg = []
                for i in range(1):
                    list_bg.append(Background(name=f'Level6Bg{i}', position=(0, 0)))
                    list_bg.append(Background(name=f'Level6Bg{i}', position=(WIN_WIDTH, 0)))
                return list_bg
            #criar mais levels



            case 'Player1':
                return Player(name='Player1', position=(10, WIN_HEIGHT / 2 - 30))
            case 'Player2':
                return Player(name='Player2', position=(10, WIN_HEIGHT / 2 + 30))
            case 'Enemy1':
                return Enemy('Enemy1', (WIN_WIDTH + 10, random.randint(40, WIN_HEIGHT - 40)))
            case 'Enemy2':
                return Enemy('Enemy2', (WIN_WIDTH + 10, random.randint(40, WIN_HEIGHT - 40)))
