from lib.thrilldigger import ThrillDigger, PlayState
from lib.thrilldigger import IncorrectStateError, GameIsOverException, UnfinishedGameException

from random import randrange

class RandomDigger(ThrillDigger):
    def execute_play_strategy(self):
        width, height = self.get_board_shape()
        bombs, rupoors = self.get_board_hazards()
        
        while self.get_play_state() == PlayState.MAKE_MOVE:
            x,y = randrange(0, width-1), randrange(0,height-1)
            self.dig(x,y)
                    






