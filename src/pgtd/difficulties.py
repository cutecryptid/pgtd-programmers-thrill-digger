from enum import IntEnum

class Difficulty(IntEnum):
    BEGINNER = 0
    INTERMEDIATE = 1
    EXPERT = 2
    CUSTOM = 3

DifficultyConfig = {
    Difficulty.BEGINNER : {
        "width" : 5,
        "height" : 4,
        "bombs" : 4,
        "rupoors" : 0,
        "price" : 30
    },
    Difficulty.INTERMEDIATE : {
        "width" : 6,
        "height" : 5,
        "bombs" : 4,
        "rupoors" : 4,
        "price" : 50
    },
    Difficulty.EXPERT : {
        "width" : 8,
        "height" : 5,
        "bombs" : 8,
        "rupoors" : 8,
        "price" : 70
    },
    Difficulty.CUSTOM : {
        "width" : 0,
        "height" : 0,
        "bombs" : 0,
        "rupoors" : 0,
        "price" : 0
    }
}