import random

VALID_CHOICES = {
    'r': 'rock (r)', 
    'p': 'paper (p)', 
    'sc': 'scissors (sc)',
    'l': 'lizard (l)', 
    'sp': 'spock (sp)'
}

def main():
    scores = {'player': 0, 'computer': 0}

    while True:
        prompt(f'Choose an abbreviation: {", ".join(VALID_CHOICES.values())}')
        player = input().strip().lower()
        valid_player = validate_choice(player)
        computer = random.choice(list(VALID_CHOICES.keys()))
        prompt(f"You chose {VALID_CHOICES[valid_player]}, Computer chose {VALID_CHOICES[computer]}")

        result = determine_result(valid_player, computer)
        prompt(result)

        update_scores(scores, result)

        prompt(f"You: {scores['player']}, Computer: {scores['computer']}")

        if scores['player'] == 3:
            prompt("You are the Champion!")
            break
        if scores['computer'] == 3:
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

def update_scores(scores, result):
    if result == "You Win!":
        scores['player'] += 1
    elif result == "Computer Wins!":
        scores['computer'] += 1

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
