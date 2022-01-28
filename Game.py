from os import system
from Player import Player

class Game:
    def __init__(self, voice=True):
        self.voice = voice
        self.player = []
        self.welcome()
        self.set_players()

    def tts(self, speak):
        if self.voice:
            system(f"termux-tts-speak {speak}")
        
        print(speak)

    def welcome(self):
        hello = "Oba, vamos jogar banco imobiliário"
        self.tts(hello)

    def set_players(self):
        who = "Digite os nomes de quem vai jogar na ordem tirada no dado"
        self.tts(who)
        
        names = input("Separe por vírgula: ")
        self.play_order = [i.strip() for i in names.split(",")]
        
        self.tts("Vão jogar:")
        for name in self.play_order:
            self.tts(name)
            self.player.append(Player(name))