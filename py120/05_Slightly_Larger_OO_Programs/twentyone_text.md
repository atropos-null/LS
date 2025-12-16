# Twenty One OOP Style

Problem: The goal of Twenty-One is to try to get as close to 21 as possible without going over. 

Nouns in italics, Verbs in bold

**Nouns**:

* *Player*
* *Dealer/Computer* 
* *Deck* (of Cards)
    * type: a list of lists with two elements, 52 total elements
        * 10 numbered cards
        * 4 suits
        * King, Jack, Queen
* *Score*
    * type: integer
    * Cards 2 - 10: value is value stated on the card
    * Monarchy suite: all cards are 10
    * Ace: 11
        - if ace at value 11 greater than 21
        - change value to 1 and add to total
* *Hand*: 
    * type: a list 
    * 2 cards given at start
* *Bookie*
    - gives a *Bank* of 5
        - for each win, plus 1
        - for each loss, minus 1
            - end game when bank == 10 or 0


**Verbs**:

* **display** greeting
* Bookie **initializes** bank
* **start** game
    - **create** deck
    - **shuffle** deck
    - **deal** two cards to both player and dealer/computer
        - player goes first:
            - **display** player their *hand* and their *current total*
            - **display** one card of the dealer/computer
            - **ask** "hit" or "stay"
                - **hit** => draw a new card
                or 
                - **stay** => turn goes to dealer/computer
                - **calculate** value of hand to constant

            - if over 21:
                - **display** total
                - **determine** winner
                - **adjust** bank
                    - +1 if win
                    - -1 if loss
                - **display** bank
                - **display** winner
        
        - if 0 < bank > 10:
            - **prompt** for new game
                - if yes,
                    - **play again**
             - if no,
                - **display** goodbye
                - **display** winnings
                - **exit** game 
        - else:
            - **display** goodbye
            - **display** winnings
            - **exit** game



Agents: Who is doing what? 

* Player
    - chooses action:
        - hit
        - stay
    - has a Hand
        - add card
        - determine value
        - shows two cards
        - sees Dealer's single card

* Dealer/Computer
    - chooses action:
        - hit until 17 is reached
    - has a Hand    
        - shows cards

* Deck
    - creates itself
    - removes used cards
    - reset deck
        - if deck goes to 0 during play, creates a new deck
    - shuffles cards
    - deals one card
    - keeps a count of how many cards are left

* Bookie:

    - creates betting line
    - tracks increases and decreases
    - displays total
    - alerts Game if the player can continue

    
* Game:

    - displays welcome greeting
    - asks Deck for deck or cards
    - asks Bookie to open the bank
    - game play begins:
        - plays one round
            - deal two hands (2 cards each)
            - update PV and DCV
            - display cards:
                - player: 2 cards, PV, 
                - show dealer: one card and state one is hidden
            - play one round:
                - ask Player:
                    - hit
                        - ask for card from Deck
                        - compute totals from hands
                        - update PV
                        - display card1, PV
                            - if PV > 21:
                                - round over, do not proceed to Dealer

                    - stay
                        - display PV
                    - game switches to DC
                        - calculates DCV
                            - if DCV > 21:
                                - round over
                            - if DCV >= 17:
                                - stay
                        
                    - determine bank
                        - if P: +1
                        - if DC: -1
                
                - start over?
                    - if yes,
                        - play one round
                    - if no,
                        - display goodbye message
                        - exit game.

            - evaluates when to end:
                - asks player: does player want to end?
                    - if yes,
                        - end
                    - if no,
                        - ask **Bookie**: is bank 0 or 10?
                        - if yes?
                            - exit game
                        - if no?
                            - play again  
    - displays goodbye greeting


Display requirements (from the assignment)

* On each player decision: show player’s hand + total; show dealer’s hand with one hidden card.
* Dealer turn: reveal hidden card, show total, and re-display after each dealer hit.
* Show results and ask to play again; welcome/goodbye messages.

Deck handling
* use same deck until no elements are left and then create fresk deck

How they would interact:

```python
# at start of each round
self.deck.reset()  # or ensure there are enough cards

# initial hands
player_hand = self.deck.deal(2)
dealer_hand = self.deck.deal(2)

# player hits
player_hand.append(self.deck.deal_one())

# dealer hits
dealer_hand.append(self.deck.deal_one())
```

Game asks Player: 
```python
def prompt_hit_or_stay(self) -> str:
    # return 'hit' or 'stay' from user input

def play_again(self) -> bool:
    # return True/False after asking the user
```

## Method lists

### Deck

```python 

class Deck:
    def __init__(self):
        # build 52 cards (4 suits × 13 ranks)
        # optionally shuffle here

    def shuffle(self):
        # random.shuffle internal list

    def deal_one(self):
        # remove and return one Card from the deck

    def deal(self, n):
        # return a list of n cards (calls deal_one n times)

    def cards_left(self):
        # return count remaining

    def reset(self):
        # rebuild a fresh 52-card deck, shuffle
```

### Bookie

```python

class Bookie:
    def __init__(self, start=5, min_balance=0, max_balance=10):
        self._balance = start
        self._min = min_balance
        self._max = max_balance

    @property
    def balance(self):
        return self._balance

    def win(self, amount=1):
        self._balance += amount

    def lose(self, amount=1):
        self._balance -= amount

    def is_broke(self):
        return self._balance <= self._min

    def is_rich(self):
        return self._balance >= self._max

    def can_continue(self):
        return not (self.is_broke() or self.is_rich())
```

### Particpant

```python
class Participant:
    def __init__(self, name):
        self.name = name
        self.hand = []  # list of Card

    def reset_hand(self):
        self.hand.clear()

    def receive(self, card):
        self.hand.append(card)

    def score(self):
        # compute total with Ace as 11, then reduce Aces to 1 as needed
        # return int
        pass

    def is_busted(self):
        return self.score() > 21

    def cards(self):
        # return a copy or iterable of all cards for display
        return list(self.hand)

```

### Player

```python
class Player(Participant):
    # No extra behavior needed beyond Participant
    # Game will ask for 'hit' or 'stay' and then call receive()
    pass
```

### Dealer

```python
class Dealer(Participant):
    def __init__(self, name="Dealer"):
        super().__init__(name)
        self._hidden = True  # first card hidden during player turn

    def hide_first_card(self):
        self._hidden = True

    def reveal_hidden(self):
        self._hidden = False

    def visible_cards(self):
        # during player turn, return [first_hidden_marker] + rest
        if not self.hand:
            return []
        if self._hidden:
            return ["<hidden>"] + self.hand[1:]
        return list(self.hand)

    def should_hit(self):
        # dealer hits while total < 17 (after reveal)
        return self.score() < 17
```

### Game

```python
class TwentyOneGame:
    def __init__(self, deck, player, dealer, bookie):
        self.deck = deck
        self.player = player
        self.dealer = dealer
        self.bookie = bookie

    def start(self):
        self.display_welcome_message()
        while True:
            self.ensure_deck_ready()
            self.play_one_round()
            self.display_bank()

            if not self.bookie.can_continue():
                break
            if not self.play_again():
                break

        self.display_goodbye_message()

    def play_one_round(self):
        self.dealer.hide_first_card()
        self.deal_initial_hands()
        self.show_initial_cards()

        self.player_turn()
        if not self.player.is_busted():
            self.dealer_turn()

        result = self.determine_result()
        self.apply_bet(result)
        self.display_result(result)

        # clear hands for next round
        self.player.reset_hand()
        self.dealer.reset_hand()

    def deal_initial_hands(self):
        # ask Deck; don’t pick cards here
        self.player.receive(self.deck.deal_one())
        self.dealer.receive(self.deck.deal_one())
        self.player.receive(self.deck.deal_one())
        self.dealer.receive(self.deck.deal_one())

    def show_initial_cards(self):
        # player: show full hand + total
        # dealer: show one card, indicate one hidden (no total yet)
        pass

    def player_turn(self):
        # loop: prompt hit/stay
        # on hit: dealer stays hidden; deal_one to player; show player hand+score
        # stop if player stays or busts
        pass

    def dealer_turn(self):
        # reveal hidden
        self.dealer.reveal_hidden()
        # show full hand + total
        # while dealer.should_hit(): deal_one, show updated hand + total
        pass

    def determine_result(self):
        # return 'player', 'dealer', or 'tie'
        pass

    def apply_bet(self, result):
        if result == 'player':
            self.bookie.win()
        elif result == 'dealer':
            self.bookie.lose()
        # tie: no change

    def ensure_deck_ready(self):
        # either reset each round, or if self.deck.cards_left() < threshold: self.deck.reset()
        pass

    # UI helpers
    def display_welcome_message(self): 
        pass
    def display_goodbye_message(self): 
        pass
    def display_result(self, result): 
        pass
    def display_bank(self): 
        pass
    def play_again(self): 
        pass
```

