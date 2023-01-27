from player import Player
from time import sleep


class Human(Player):
    def __init__ (self, name):
        super().__init__(name)
        self.score = 0
        self.name = name

    def choose_gesture(self):
        user_choice = int(input("press 0 for rock, 1 for paper, 2 for scissors, , 3 for spock, 4 for lizard "))
        self.chosen_gesture = self.list_of_gestures[user_choice] #provides a random selection from the list.

        sleep(1) # Delays execution.
        print(f'{self.name} has selected {self.chosen_gesture}')