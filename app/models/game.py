

class Game:
    
    
    def play_game(self, player1_choice, player1_name, player2_choice, player2_name):
        if player1_choice == "rock" and player2_choice =="scissors":
            return f"{player1_name}wins by playing rock!"
        elif player1_choice == "scissors" and player2_choice =="rock":
            return "Rock wins!"
        elif player1_choice == "paper" and player2_choice =="rock":
            return "Paper wins!"
        elif player1_choice == "rock" and player2_choice =="paper":
            return "Paper wins!"
        elif player1_choice == "scissors" and player2_choice =="paper":
            return "Scissors wins!"
        elif player1_choice == "paper" and player2_choice =="scissors":
            return "Scissors wins!"
        elif player1_choice == player2_choice:
            return "It's a draw!"

        
            

