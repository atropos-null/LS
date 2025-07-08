import random
import os
import sys

INITIAL_MARKER = ' '
HUMAN_MARKER = 'X'
COMPUTER_MARKER = 'O'

def prompt(message):
    print(f"=> {message}")

def play_again():
    prompt("Play again? (y or n)")
    answer = input().lower()
    return answer and answer[0] == 'y'

def display_board(board):
    os.system('clear')
    prompt(f"You are {HUMAN_MARKER}. Computer is {COMPUTER_MARKER}.")
    print('')
    print('     |     |')
    print(f"  {board[1]}  |  {board[2]}  |  {board[3]}")
    print('     |     |')
    print('-----+-----+-----')
    print('     |     |')
    print(f"  {board[4]}  |  {board[5]}  |  {board[6]}")
    print('     |     |')
    print('-----+-----+-----')
    print('     |     |')
    print(f"  {board[7]}  |  {board[8]}  |  {board[9]}")
    print('     |     |')
    print('')

def initialize_board():
    return {square: INITIAL_MARKER for square in range(1, 10)}

def empty_squares(board):
    return [key for key, value in board.items() if value == INITIAL_MARKER]

def join_or(lst, delimiter=', ', word='or'):
    if not lst:
        return ""
    temp = [str(element) for element in lst]
    if len(lst) == 1:
        return str(lst[0]) 
    elif len(lst) == 2:
        return f"{temp[0]} {word} {temp[1]}"
    else: 
        leading_values = delimiter.join(temp[0:-1])
        return f"{leading_values}{delimiter}{word} {temp[-1]}"

def player_chooses_square(board):
    while True:
        valid_choices = [str(num) for num in empty_squares(board)]
        prompt(f"Choose a square ({join_or(valid_choices)}):")
        square = input().strip()
        if square in valid_choices:
            break
        prompt("Sorry, that's not a valid choice.")
    board[int(square)] = HUMAN_MARKER

def computer_chooses_square(board):
    if len(empty_squares(board)) == 0:
        return
    square = random.choice(empty_squares(board))
    board[square] = COMPUTER_MARKER

def board_full(board):
    return len(empty_squares(board)) == 0

def someone_won(board):
    return bool(detect_winner(board))

def detect_winner(board):
    winning_lines = [
        [1, 2, 3], [4, 5, 6], [7, 8, 9],  # rows
        [1, 4, 7], [2, 5, 8], [3, 6, 9],  # columns
        [1, 5, 9], [3, 5, 7]              # diagonals
    ]
    for line in winning_lines:
        sq1, sq2, sq3 = line
        if (board[sq1] == HUMAN_MARKER
                and board[sq2] == HUMAN_MARKER
                and board[sq3] == HUMAN_MARKER):
            return 'Player'
        elif (board[sq1] == COMPUTER_MARKER
                and board[sq2] == COMPUTER_MARKER
                and board[sq3] == COMPUTER_MARKER):
            return 'Computer'
    return None

def print_final_scores(player_score, computer_score, ties):
    prompt(f"Final Scores: Player {player_score}, Computer {computer_score}, Ties {ties}")
    if player_score > computer_score:
        prompt("Player wins the match!")
    elif computer_score > player_score:
        prompt("Computer wins the match!")
    else:
        prompt("It's a tie! No one wins ¯\_(ツ)_/¯")

def play_tic_tac_toe():
    player_score = 0
    computer_score = 0
    ties = 0

    for round_num in range(1, 6):
        board = initialize_board()
        while True:
            display_board(board)
            player_chooses_square(board)
            if someone_won(board) or board_full(board):
                break
            computer_chooses_square(board)
            if someone_won(board) or board_full(board):
                break

        display_board(board)
        winner = detect_winner(board)
        if winner == 'Player':
            prompt("Player won this round!")
            player_score += 1
        elif winner == 'Computer':
            prompt("Computer won this round!")
            computer_score += 1
        else:
            prompt("It's a tie!")
            ties += 1
        prompt(f"Score after round {round_num}: Player {player_score}, Computer {computer_score}, Ties {ties}")

        if round_num < 5:
            if not play_again():
                print_final_scores(player_score, computer_score, ties)
                sys.exit()

    print_final_scores(player_score, computer_score, ties)

while True:
    play_tic_tac_toe()
    if not play_again():
        break