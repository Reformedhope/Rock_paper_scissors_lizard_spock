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
            
            if self.human.choose_gesture == "rock" and self.ai.choose_gesture == "scissors ":
                print("Rock smashed the scissors")
            elif self.human.choose_gesture == "scissors" and self.ai.choose_gesture == "rock":
                print("Rock smashed the scissors")
            elif self.human.choose_gesture == "scissors" and self.ai.choose_gesture == "paper":
                print("scissors cuts paper")
            elif self.human.choose_gesture == "paper" and self.ai.choose_gesture == "scissors":
                print("scissors cuts paper")
            elif self.human.choose_gesture == "paper" and self.ai.choose_gesture == "rock":
                print("paper covers rock")
            elif self.human.choose_gesture == "rock" and self.ai.choose_gesture == "paper":
                print("paper covers rock")
            elif self.human.choose_gesture == "rock" and self.ai.choose_gesture == "lizard":
                print("rock crushes lizard")
            elif self.human.choose_gesture == "lizard" and self.ai.choose_gesture == "rock":
                print("rock crushes lizard")
            elif self.human.choose_gesture == "lizard" and self.ai.choose_gesture == "spock":
                print("lizard poisons spock")
            elif self.human.choose_gesture == "spock" and self.ai.choose_gesture == "lizard":
                print("lizard poisons spock")
            elif self.human.choose_gesture == "spock" and self.ai.choose_gesture == "Scissors":
                print("spock smashes scissors")
            elif self.human.choose_gesture == "scissors" and self.ai.choose_gesture == "spock":
                print("spock smashes scissors")
            elif self.human.choose_gesture == "scissors" and self.ai.choose_gesture == "lizard":
                print("scissors decapitates lizard")
            elif self.human.choose_gesture == "lizard" and self.ai.choose_gesture == "scissors":
                print("scissors decapitates lizard")
            elif self.human.choose_gesture == "lizard" and self.ai.choose_gesture == "paper":
                print("lizard eats paper")
            elif self.human.choose_gesture == "paper" and self.ai.choose_gesture == "spock":
                print("paper disproves spock")
            elif self.human.choose_gesture == "spock" and self.ai.choose_gesture == "paper":
                print("paper disproves")
            elif self.human.choose_gesture == "spock" and self.ai.choose_gesture == "rock":
                print("spock vaporized rock")
            elif self.human.choose_gesture == "rock" and self.ai.choose_gesture == "spock":
                print("spock vaporizes rock")
            else:
                print("tie, try again.")

    
             

            #main battle above, duplicates below. 

            # elif self.human.choose_gesture == "rock" and self.ai.choose_gesture == "rock":
            #     print("Tie, try again ")
            # elif self.human.choose_gesture == "scissors" and self.ai.choose_gesture == "scissors":
            #     print("Tie, try again")
            # elif self.human.choose_gesture == "paper" and self.ai.choose_gesture == "paper":
            #     print("Tie, try again")
            # elif self.human.choose_gesture == "spock" and self.ai.choose_gesture == "spock":
            #     print("Tie, try again")
            # elif self.human.choose_gesture == "lizard" and self.ai.choose_gesture == "lizard":
            #     print("Tie, try again")  
            
              



    def display_winner(self):
        pass



                