import random

VALID_CHOICES = {
    'r' : 'rock (r)', 
    'p' : 'paper (p)', 
    'sc' : 'scissors (sc)',
    'l': 'lizard (l)', 
    'sp': 'spock (sp)'
}

def main():

    player_score = 0
    computer_score = 0

    while True:

        prompt(f'Choose an abbrevation: {", ".join(VALID_CHOICES.values())}')
        player = input().strip().lower()
        valid_player = validate_choice(player)
        computer = random.choice(list(VALID_CHOICES.keys()))
        prompt(f"You chose {valid_player}, Computer chose {computer}")

        result = determine_result(valid_player, computer)
        prompt(result)

        if result == "You Win!":
            player_score += 1
        elif result == "Computer Wins!":
            computer_score += 1

        prompt(f"You: {player_score}, Computer: {computer_score}")

        if player_score == 3:
            prompt("You are the Champion!")
            break
        if computer_score == 3:
            prompt("The Computer is the Champion!")
            break

        if not get_playagain():
            prompt("Goodbye!")
            break

def prompt(message):
    print(f"==> {message}")
    return ""

def validate_choice(player):
    while player not in VALID_CHOICES:
        prompt("That's not a valid choice")
        prompt(f'Choose one: {", ".join(VALID_CHOICES.values())}')
        player = input().strip().lower()
    return player

def determine_result(valid_player, computer):

    match(valid_player, computer):

        case ('r', 'sc') | ('p', 'r') | ('sc', 'p') | ('r', 'l') | \
             ('l', 'sp') | ('sp', 'sc') | ('sp', 'r') | ('l', 'p') | \
             ('sc', 'l') | ('p', 'sp') | ('r', 'l'):
            return "You Win!"

        case ('sc', 'r') | ('r', 'p') | ('p', 'sc') | ('l', 'r') | \
             ('sp', 'l') | ('sc', 'sp') | ('r', 'sp') | ('p', 'l') | \
             ('l', 'sc') | ('sp', 'p') | ('l', 'r'):
            return "Computer Wins!"

        case _:
            return "It is a tie!"


def get_playagain():

    answer = input(prompt('Do you want to play again? (y/n)? ')).lower()

    while True:

        if answer.startswith('n'):
            return False
        if answer.startswith('y'):
            return True

        prompt("That's not a valid choice")
        answer = input(prompt('Do you want to play again? (y/n)? ')).lower()

main()