import random

class Player:

    CHOICES = ('rock', 'paper', 'scissors', 'lizard', 'spock')

    def __init__(self):
        self.move = None
        self.score = 0

class Computer(Player):


    def __init__(self):
        super().__init__()

    def choose(self):
        self.move = random.choice(Player.CHOICES)

class Human(Player):

    def __init__(self):
        super().__init__()

    def choose(self):
        while True:
            choice = input("Please choose rock, paper, scissors, lizard, or Spock: ").strip().lower()
            if choice in Player.CHOICES:
                break
            print(f'Sorry, {choice} is not valid')
        self.move = choice

class RPSGame:

    TARGET_SCORE = 5

    def __init__(self):
        self._human = Human()
        self._computer = Computer()
        self._history = []

    def _reset_scores(self):
        self._human.score = 0
        self._computer.score = 0
        self._history = []  # clear history for each new match
    
    def _display_welcome_message(self):
        print("Welcome to Rock Paper Scissors!")

    def _display_goodbye_message(self):
        print("Thanks for playing Rock Paper Scissors!")

    def _human_wins(self):

        return self._beats(self._human.move, self._computer.move)

    def _computer_wins(self):

        return self._beats(self._computer.move, self._human.move)
    
    def _beats(self, a, b):
        return ((a == 'rock'     and b in ('scissors', 'lizard')) or
            (a == 'paper'    and b in ('rock', 'spock')) or
            (a == 'scissors' and b in ('paper', 'lizard')) or
            (a == 'lizard'   and b in ('spock', 'paper')) or
            (a == 'spock'    and b in ('scissors', 'rock')))
    

    def _display_winner(self, winner):
        print(f"You chose {self._human.move}")
        print(f"The Computer chose: {self._computer.move}")

        if winner is self._human:
            print("You win!")
        elif winner is self._computer:
            print("Computer Wins!")
        else:
            print("It's a tie")

        print(f"Score — You: {self._human.score}  Computer: {self._computer.score}")

    def _display_scores(self):
        print(f"Score — You: {self._human.score}  Computer: {self._computer.score}")
    
    def _round_winner(self):
        if self._human_wins():
            return self._human
        if self._computer_wins():
            return self._computer
        return None
    
    def _display_grand_winner(self):
        if self._human.score > self._computer.score:
          print("You won the match!")
        else:
            print("Computer won the match!")

    def _play_again(self):
        answer = input("Would you like to play again? ('y'/'n') ").lower()
        return answer.startswith("y")

    def play(self):
        self._display_welcome_message()

        while True:  # match loop
            self._reset_scores()

            while not self._reached_target():  # round loop
                self._human.choose()
                self._computer.choose()

                winner = self._round_winner()   
                self._award_point(winner)
                self._display_winner(winner)
                self._record_history(winner)

            self._display_grand_winner()
            self._display_history() 

            if not self._play_again():
                break

        self._display_goodbye_message()

   
    def _award_point(self, winner):
        if winner is not None:
            winner.score += 1

    def _reached_target(self):
        return (self._human.score >= self.TARGET_SCORE or
                self._computer.score >= self.TARGET_SCORE)

    def _record_history(self, winner):
        if winner is self._human:
            result = 'human'
        elif winner is self._computer:
            result = 'computer'
        else:
            result = 'tie'

        self._history.append({
        'human': self._human.move,
        'computer': self._computer.move,
        'result': result,
        'score': (self._human.score, self._computer.score), 
        })

    def _display_history(self):
        print("Round history:")
        for i, entry in enumerate(self._history, 1):
            h, c = entry['human'], entry['computer']
            r = entry['result']
            s_h, s_c = entry['score']
            print(f"  {i}. you={h}, computer={c}, result={r}, score={s_h}-{s_c}")

RPSGame().play()