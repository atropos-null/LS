import random

VALID_CHOICES = ["rock", "paper", "scissors"]


def get_player_choice():
    while True:
        print(f"Choose one: {', '.join(VALID_CHOICES)}")
        choice = input().strip().lower()
        if choice in VALID_CHOICES:
            return choice
        print("That's not a valid choice")

def get_play_again():
   
    while True:
        print("Do you want to play again (y/n)?")
        answer = input().strip().lower()
        if answer.startswith("y"):
            return True
        elif answer.startswith("n"):
            return False
        print("That's not a valid choice")

def display_winner(player, computer):
    print(f"You chose {player}, computer chose {computer}")

    if ((player == "rock" and computer == "scissors") or
        (player == "paper" and computer == "rock") or
        (player == "scissors" and computer == "paper")):
        print("You win!")
    elif ((player == "rock" and computer == "paper") or
          (player == "paper" and computer == "scissors") or
          (player == "scissors" and computer == "rock")):
        print("Computer wins!")
    else:
        print("It's a tie!")

def play_game():
    while True:
        player_choice = get_player_choice()
        computer_choice = random.choice(VALID_CHOICES)
        display_winner(player_choice, computer_choice)
        if not get_play_again():
            break

if __name__ == "__main__":
     play_game()


"""

A bare bones approach:

def rps(p1, p2):

    choices = ['rock', 'paper', 'scissors']
    
    if p1 not in choices and p2 not in choices:
        return "Draw!"    
    if p1 not in choices:
        return "Player 2 won!"
    if p2 not in choices:
        return "Player 1 won!"

    # Draw
    if p1 == p2:
        return "Draw!"
    # All possible win conditions
    if (p1 == 'rock' and p2 == 'scissors') or \
       (p1 == 'scissors' and p2 == 'paper') or \
       (p1 == 'paper' and p2 == 'rock'):
        return "Player 1 won!"
    else:
        return "Player 2 won!"

"""