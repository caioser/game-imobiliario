from turtle import position
from unicodedata import name


class Propertie:
    def __init__(self, name, country, price, position):
        self.name = name
        self.country = country
        self.price = price
        self.board_position = position
