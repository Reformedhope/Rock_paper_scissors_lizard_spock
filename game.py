from player import Player
from human import Human
from ai import AI

class Game:

    def __init__(self):
     self.player_one = None
     self.player_two = None

    def display_rules(self):
       print(' The game will be played with best 2 out of 3. choose your options wisely.')
    
    def Choose_players(self):
        user_choice = input('Select how many people are going to play, Option 1 or 2 ')
        if user_choice =="1":
            user_one_name = input('what is player ones name? ')
            self.player_one = Human(user_one_name)
            self.player_two = AI ("Ben")
        if user_choice =="2":
            user_one_name = input ("what is player ones name? ")
            user_two_name = input('what is player twos name? ')
            self.player_one = Human(user_one_name)
            self.player_two = Human (user_two_name)
        
        
                

       
    
    def run_game(self):
        self.display_rules()
        self.Choose_players()
        self.play_rounds()
        self.display_winner()

    def play_rounds(self):


        while self.player_two.score < 3 and self.player_one.score < 3:
            self.player_one.choose_gesture()
            self.player_two.choose_gesture()
            
           
            if self.player_two.chosen_gesture == "rock" and self.player_one.chosen_gesture == "scissors":
                print("Rock smashed the scissors")
                self.player_two.score += 1
                
            elif self.player_two.chosen_gesture == "scissors" and self.player_one.chosen_gesture == "rock":
                print("Rock smashed the scissors")
                self.player_one.score += 1

            elif self.player_two.chosen_gesture == "scissors" and self.player_one.chosen_gesture == "paper":
                print("scissors cuts paper")
                self.player_two.score += 1

            elif self.player_two.chosen_gesture == "paper" and self.player_one.chosen_gesture == "scissors":
                print("scissors cuts paper")
                self.player_one.score += 1

            elif self.player_two.chosen_gesture == "paper" and self.player_one.chosen_gesture == "rock":
                print("paper covers rock")
                self.player_two.score += 1

            elif self.player_two.chosen_gesture == "rock" and self.player_one.chosen_gesture == "paper":
                print("paper covers rock")
                self.player_one.score += 1

            elif self.player_two.chosen_gesture == "rock" and self.player_one.chosen_gesture == "lizard":
                print("rock crushes lizard")
                self.player_two.score += 1 


            elif self.player_two.chosen_gesture == "lizard" and self.player_one.chosen_gesture == "rock":
                print("rock crushes lizard")
                self.player_one.score += 1

            elif self.player_two.chosen_gesture == "lizard" and self.player_one.chosen_gesture == "spock":
                print("lizard poisons spock")
                self.player_two.score += 1

            elif self.player_two.chosen_gesture == "spock" and self.player_one.chosen_gesture == "lizard":
                print("lizard poisons spock")
                self.player_one.score += 1

            elif self.player_two.chosen_gesture == "spock" and self.player_one.chosen_gesture == "scissors":
                print("spock smashes scissors")


            elif self.player_two.chosen_gesture == "scissors" and self.player_one.chosen_gesture == "spock":
                print("spock smashes scissors")
                self.player_one.score += 1

            elif self.player_two.chosen_gesture == "scissors" and self.player_one.chosen_gesture == "lizard":
                print("scissors decapitates lizard")


            elif self.player_two.chosen_gesture == "lizard" and self.player_one.chosen_gesture == "scissors":
                print("scissors decapitates lizard")
                self.player_one.score += 1

            elif self.player_two.chosen_gesture == "lizard" and self.player_one.chosen_gesture == "paper":
                print("lizard eats paper")
                self.player_two.score += 1

            elif self.player_two.chosen_gesture == "paper" and self.player_one.chosen_gesture == "spock":
                print("paper disproves spock")
                self.player_two.score += 1

            elif self.player_two.chosen_gesture == "spock" and self.player_one.chosen_gesture == "paper":
                print("paper disproves")
                self.player_one.score += 1

            elif self.player_two.chosen_gesture == "spock" and self.player_one.chosen_gesture == "rock":
                print("spock vaporized rock")
                self.player_two.score += 1

            elif self.player_two.chosen_gesture == "rock" and self.player_one.chosen_gesture == "spock":
                print("spock vaporizes rock")
                self.player_one.score += 1

            elif self.player_two.chosen_gesture == "rock" and self.player_one.chosen_gesture == "rock":
                print("Tie, try again. ")

            elif self.player_two.chosen_gesture == "scissors" and self.player_one.chosen_gesture == "scissors":
                print("Tie, try again.")

            elif self.player_two.chosen_gesture == "paper" and self.player_one.chosen_gesture == "paper":
                print("Tie, try again.")

            elif self.player_two.chosen_gesture == "spock" and self.player_one.chosen_gesture == "spock":
                print("Tie, try again.")

            elif self.player_two.chosen_gesture == "lizard" and self.player_one.chosen_gesture == "lizard":
                print("Tie, try again.")
            
    
            
              



    def display_winner(self):
        if self.player_one.score <= 2:
            print(" Player one wins! ")

        if self.player_two.score <= 2:
            print( "player two wins! ")



                