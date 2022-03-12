from strats.randomstrategy import RandomDigger
from lib.difficulties import Difficulty

'''
Instances a digger and runs it once. Just that.
'''

digger = RandomDigger(Difficulty.EXPERT)
victory = digger.play()

if victory:
    print("VICTORY!")
else:
    print("DEFEAT...")

print(f"SCORE: {digger.get_score()}")
print(digger.get_pretty_board())
