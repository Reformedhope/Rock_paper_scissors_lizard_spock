from player import Player
from ai import AI
from human import Human

class Game:

    def __init__(self):
     self.ai = AI
     self.human =Human

    def display_rules(self):
        print('Select how many people are going to play, Option 1, 2, or if you select 3 some hocus pocus harry potter magic will happen')
        print(' The game will be played with best 2 out of 3. choose your options wisely.')
    def run_game(self):
        while self.human.score >= 0 and self.ai.score >=0:
            
            if self.human.choose_gesture == "scissors":




    # def display_winner(self):
    #     pass




       
    
