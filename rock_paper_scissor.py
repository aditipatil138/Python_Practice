import random

def game():
    user_input = input("Enter your choice, 'r' for rock, 'p' for paper and 's' for scissor, What is it going to be? ")
    computer_choice = random.choice(['r', 's', 'p'])

    if user_input ==  computer_choice:
        return "Its a Tie! Win Win"
    if is_win(user_input, computer_choice):
        return "Congratulations!!!!! You Won!"
    return "Better luck next time! Computer Won!"
    
def is_win(player, opponent):
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 's'):
        return True
    
print(game())