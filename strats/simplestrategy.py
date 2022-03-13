from pgtd import ThrillDigger
from pgtd import IncorrectStateError, GameIsOverError, UnfinishedGameError
'''
Simple Strategy for thrilldigger that digs up the board sequentially.

Pretty bad strat imho.
'''

class SimpleDigger(ThrillDigger):
    def execute_play_strategy(self):
        width, height = self.get_board_shape()
        bombs, rupoors = self.get_board_hazards()
        try:
            for x in range(0,height):
                for y in range(0,width):
                    self.dig(x,y)
                    
        except GameIsOverError as e:
            pass


