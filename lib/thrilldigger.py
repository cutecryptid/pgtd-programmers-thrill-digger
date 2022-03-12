from enum import IntEnum
from lib.exceptions import *
from lib.board import Board, Item
from lib.difficulties import Difficulty, DifficultyConfig

class PlayState(IntEnum):
    MAKE_MOVE = 0
    FAILED = 1
    VICTORY = 2

class ThrillDigger:
    __board = None

    __score = 0
    __state = PlayState.MAKE_MOVE

    __dug_up = 0
    __size = 0
    __hazards = 0
    __price = 0

    def __init__(self, difficulty: Difficulty, width = 0, height = 0, bombs = 0, rupoors = 0, price = 0):
        config = DifficultyConfig[difficulty]
        if difficulty == Difficulty.CUSTOM:
            config["width"] = width
            config["height"] = height
            config["bombs"] = bombs
            config["rupoors"] = rupoors
            config["price"] = price

        self.__hazards = config["bombs"] + config["rupoors"]
        self.__size = config["width"] * config["height"]
        self.__price = config["price"]
        self.__board = Board(config["width"], config["height"], config["bombs"], config["rupoors"])

    def play(self):
        self.execute_play_strategy()
        if self.__state == PlayState.VICTORY:
            return True
        elif self.__state == PlayState.FAILED:
            return False
        else:
            raise UnfinishedGameException("Strategy finished without winning or losing")

    def dig(self,x,y):
        if (self.__state != PlayState.MAKE_MOVE):
            raise GameIsOverException("Game already finished")
        item = self.__board.dig(x,y)
        if item != Item.RUPOOR or item != Item.RUPOOR:
            self.__dug_up += 1
        if item == Item.BOMB:
            self.__state = PlayState.FAILED
        else:
            self.__score = max(0, self.__score + int(item))
            self.__state = PlayState.MAKE_MOVE
            if (self.__size - self.__hazards) == self.__dug_up:
                self.__state = PlayState.VICTORY
        return item
    
    def get_price(self):
        return self.__price

    def get_score(self):
        return self.__score
    
    def get_play_state(self):
        return self.__state
    
    def get_board(self):
        return self.__board.get_board()
    
    def get_pretty_board(self):
        return str(self.__board)
    
    def get_board_shape(self):
        return self.__board.get_shape()
    
    def get_board_hazards(self):
        return self.__board.get_hazards()

    def execute_play_strategy(self):
        pass