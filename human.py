from player import Player
from time import sleep


class Human(Player):
    def __init__ (self, name):
        super().__init__()
        self.score = 0
        self.name = name

    def choose_gesture(self):
        self.chosen_gesture = str(0,4) #provides a random selection from the list.
        gesture_list = ["Rock", "Paper", "scissor", "Lizard", "Spock"] # provids the list of options for the player to choose from. 
        sleep(1) # Delays execution.
        print(f'{self.name} has selected {gesture_list[int(self.chosen_gesture)]}')