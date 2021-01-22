
class Game:
    
    
    def play_game(self, player1_choice, player2_choice):
        if player1_choice == "rock" and player2_choice =="scissors":
            result = "Player 1 wins by playing rock"
            return result
        elif player1_choice == "scissors" and player2_choice =="rock":
            result = "Player 2 wins by playing rock"
            return result
        elif player1_choice == "paper" and player2_choice =="rock":
            result = "Player 1 wins by playing paper"
            return result
        elif player1_choice == "rock" and player2_choice =="paper":
            result = "Player 2 wins by playing paper"
            return result
        elif player1_choice == "scissors" and player2_choice =="paper":
            result = "Player 1 wins by playing scissors"
            return result
        elif player1_choice == "paper" and player2_choice =="scissors":
            result = "Player 1 wins by playing scissors"
            return result
        elif player1_choice == player2_choice:
            return none 

        
            

