from thrilldigger import ThrillDigger

class SimpleDigger(ThrillDigger):
    def play_strategy(self):
        print(self.probe(0,0))

digger = SimpleDigger(3,3,1,0)
victory, score = digger.play()

print(victory, score)