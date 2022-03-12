from strats.simplestrategy import SimpleDigger
from lib.difficulties import Difficulty

iterations = 10000
difficulty = Difficulty.EXPERT

victories = 0
defeats = 0
total_score = 0
for i in range(iterations):
    print(f"#{i+1} [{victories}-{defeats}] <{total_score}>")
    digger = SimpleDigger(difficulty)
    victory = digger.play()
    if victory:
        victories += 1
    else:
        defeats += 1
    total_score += digger.get_score() - digger.get_price()
    print(digger.get_pretty_board())

avg_cost = digger.get_price()
avg_return = total_score / iterations

avg_roi = (avg_return / avg_cost)*100

print(f"TOTAL: [{victories}-{defeats}] <{total_score} | {avg_return:.2f}> ROI: {avg_roi:.2f}%")