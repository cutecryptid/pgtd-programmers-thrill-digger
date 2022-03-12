from random import sample
from enum import IntEnum

class Items(IntEnum):
    BLANK = -1
    BOMB = 0
    RUPOOR = -20
    GREEN = 1
    BLUE = 5
    RED = 20
    SILVER = 100
    GOLDEN = 300

item_danger = [ Items.GREEN, Items.BLUE, Items.BLUE, Items.RED, Items.RED,
                Items.SILVER, Items.SILVER, Items.GOLDEN, Items.GOLDEN ]

item_code = {
    Items.BLANK : " ",
    Items.GREEN : "G",
    Items.BLUE : "B",
    Items.RED : "R",
    Items.SILVER : "S",
    Items.GOLDEN : "*",
    Items.BOMB : "X",
    Items.RUPOOR : "-"
}

class CellState(IntEnum):
    COVERED = 0
    UNCOVERED = 1
    FLAGGED = 2

class Board():
    __board = []
    __playboard = []

    __width = 0
    __height = 0
    __bombs = 0
    __rupoors = 0

    def __init__(self, width, height, bombs, rupoors):
        self.__width = width
        self.__height = height
        self.__bombs = bombs
        self.__rupoors = rupoors

        board_coordinates = [(x, y) for x in range(0,self.__height) for y in range(0, self.__width)]
        bombs_coordinates = sample(board_coordinates, self.__bombs)
        remaining_coordinates = [a for a in board_coordinates if a not in bombs_coordinates]
        rupoors_coordinates = sample(remaining_coordinates, self.__rupoors)

        self.__playboard = [[CellState.COVERED for i in range(0,self.__width)] for j in range(0,self.__height)]
        self.__board = [[Items.BLANK for i in range(0,self.__width)] for j in range(0,self.__height)]

        for bomb in bombs_coordinates:
            x,y = bomb
            self.__board[x][y] = Items.BOMB
        for rupoor in rupoors_coordinates:
            x,y = rupoor
            self.__board[x][y] = Items.RUPOOR

        for x,row in enumerate(self.__board):
            for y,cell in enumerate(row):
                neighbors = [(x-1,y),(x-1,y+1),(x,y-1),(x+1,y-1),(x+1,y),(x+1,y+1),(x,y+1),(x-1,y-1)]
                hazard = 0
                for n in neighbors:
                    nx, ny = n
                    if 0 <= nx <= self.__height-1 and 0 <= ny <= self.__width-1:
                        item = self.__board[nx][ny]
                        if item == Items.BOMB or item == Items.RUPOOR:
                            hazard +=1
                if cell != Items.BOMB and cell != Items.RUPOOR:
                    self.__board[x][y] = item_danger[hazard]

    def dig(self,x,y):
        item = self.__board[x][y]
        self.__playboard[x][y] = CellState.UNCOVERED
        return item
    
    def cell_state(self,x,y):
        return self.__playboard[x][y]
    
    def get_board(self):
        board = [[(CellState.COVERED, Items.BLANK) for i in range(0,self.__width)] for j in range(0,self.__height)]
        for x,row in enumerate(self.__playboard):
            for y,cell in enumerate(row):
                if cell == CellState.UNCOVERED:
                    board[x][y] = (CellState.UNCOVERED, self.__board[x][y])
        return board
    
    def get_shape(self):
        return (self.__width, self.__height)
    
    def get_hazards(self):
        return (self.__bombs, self.__rupoors)
    
    def __str__(self):
        ret = ""
        board = self.get_board()
        for x,row in enumerate(board):
            for y,cell in enumerate(row):
                state, item = cell
                if state == CellState.UNCOVERED:
                    ret += f"[{item_code[item]}]"
                else:
                    ret += "[ ]"
            ret += "\n"
        return ret