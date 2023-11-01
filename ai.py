from player import Player
import random
from time import sleep

class AI(Player):

    def __init__ (self, name):
        super().__init__(name)
        self.score = 0
        self.name = name

    def choose_gesture(self):
        gesture = random.choice(self.list_of_gestures) #provides a random selection from the list.

        sleep(1) # Delays execution.
        print(f'{self.name} has picked {gesture}')

        return gesture
