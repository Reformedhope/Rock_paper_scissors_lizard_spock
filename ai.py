from player import Player
import random
from time import sleep

class AI(Player):

    def __init__ (self, name):
        super().__init__()
        self.score = 0
        self.name = name

    def choose_gesture(self):
        self.chosen_gesture = str(random.randint(0,4)) #provides a random selection from the list.
        gesture_list = ["Rock", "Paper", "scissor", "Lizard", "Spock"]
        sleep(1) # Delays execution.
        print(f'{self.name} has picked{gesture_list[int(self.chosen_gesture)]}')
