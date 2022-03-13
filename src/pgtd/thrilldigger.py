from enum import IntEnum
from .exceptions import *
from .board import Board, Item, CellState
from .difficulties import Difficulty, DifficultyConfig

class PlayState(IntEnum):
    INITIAL_STATE = 0
    MAKE_MOVE = 1
    FAILED = 2
    VICTORY = 3

class ThrillDigger:
    __board = None
    __price = 0

    __score = 0
    __dug_up = 0
    __state = PlayState.INITIAL_STATE

    def __init__(self, difficulty: Difficulty, width = 0, height = 0, bombs = 0, rupoors = 0, price = 0):
        config = DifficultyConfig[difficulty]
        if difficulty == Difficulty.CUSTOM:
            config["width"] = width
            config["height"] = height
            config["bombs"] = bombs
            config["rupoors"] = rupoors
            config["price"] = price

        self.__price = config["price"]
        self.__board = Board(config["width"], config["height"], config["bombs"], config["rupoors"])
    
    def reset(self):
        self.__state = PlayState.INITIAL_STATE
        width, height = self.__board.get_shape()
        bombs, rupoors = self.__board.get_hazards()
        self.__score = 0
        self.__dug_up = 0
        self.__board = Board(width, height, bombs, rupoors)

    def play(self):
        if (self.__state != PlayState.INITIAL_STATE):
            raise GameAlreadyStartedError("Some holes have been previously dug up")
        self.execute_play_strategy()
        if self.__state == PlayState.VICTORY:
            return True
        elif self.__state == PlayState.FAILED:
            return False
        else:
            raise UnfinishedGameError("Strategy finished without winning or losing")

    def dig(self,x,y):
        if (self.__state == PlayState.VICTORY or  self.__state == PlayState.FAILED):
            raise GameIsOverError("Game already finished")
        previous_state = self.__board.cell_state(x,y)
        item = self.__board.dig(x,y)
        # Dug up only increases if we dig up treasure and we didn't already dug up that cell
        if item != Item.RUPOOR or item != Item.RUPOOR:
            if previous_state == CellState.COVERED:
                self.__dug_up += 1
        if item == Item.BOMB:
            self.__state = PlayState.FAILED
        else:
            # Only increase score if we didn't previously dug up that item
            if previous_state == CellState.COVERED:
                self.__score = max(0, self.__score + int(item))
            self.__state = PlayState.MAKE_MOVE
            width, height = self.__board.get_shape()
            bombs,rupoors = self.__board.get_hazards()
            if ((width*height)-(bombs+rupoors)) == self.__dug_up:
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