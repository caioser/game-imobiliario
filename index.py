import json
import random
import subprocess
from Dice import Dice

class GameFlow():
    def __init__(self) -> None:
        self.state = 'ready'

    def setState(self) -> None:
        text = '[ENTER]: continuar...'
        state = input(text)

class Player():
    def __init__(self, name) -> None:
        self.name = name
        self.money = 805
        self.pos = 0

player = []


with open('board.json', 'r') as file:
    tabuleiro = json.loads(file.read())

print(tabuleiro[5])