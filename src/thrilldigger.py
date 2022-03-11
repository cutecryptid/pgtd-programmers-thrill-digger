import numpy as np
from enum import Enum

class PlayState(Enum):
    START = 0
    MAKE_MOVE = 1
    FAILED = 2
    VICTORY = 3

class Items(Enum):
    BOMB = 0
    RUPOOR = -20
    GREEN = 1
    BLUE = 5
    RED = 20
    SILVER = 100
    GOLDEN = 300

class Board():
    def __init__(self, width, height, bombs, rupoors):
        pass
    
    def probe(self,x,y):
        return Items.BOMB

class ThrillDigger:
    __board = None

    __score = 0
    __state = PlayState.START

    def __init__(self, width, height, bombs, rupoors):
        self.__board = Board(width, height, bombs, rupoors)

    
    def play(self):
        if self.__state == PlayState.START:
            self.play_strategy()
            if self.__state == PlayState.VICTORY:
                return (True, self.__score)
            elif self.__state == PlayState.FAILED:
                return (False, self.__score)
            else:
                raise ValueError(f"Incorrect End State: {self.__state}")
        else:
            raise ValueError(f"Incorrect PlayState: {self.__state}")

    
    def probe(self,x,y):
        item = self.__board.probe(x,y)
        if item == Items.BOMB:
            self.__state = PlayState.FAILED
        else:
            self.__score = min(0, self.__score + item)
            self.__state = PlayState.MAKE_MOVE
            if (self.__board.check_victory()):
                self.__state = PlayState.VICTORY
        return (item, self.__state)

    
    def check_victory(self):
        return False
        

    def play_strategy(self):
        pass