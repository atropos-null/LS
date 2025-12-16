import random
   
class Deck:
    
    SUITS = ('Diamonds', 'Hearts', 'Clubs', 'Spades')
    VALUES = {'Ace': 11, 
                   'Two': 2, 
                   'Three': 3, 
                   'Four': 4, 
                   'Five': 5, 
                   'Six': 6, 
                   'Seven': 7, 
                   'Eight': 8, 
                   'Nine': 9, 
                   'Ten': 10,
                   'Jack': 10,
                   'Queen': 10,
                   'King': 10
                   }
    
    def __init__(self):
        self.reset()

    def reset(self):
        # store internally; each card can be a tuple or small object
        self.cards = [ (f"{rank} of {suit}", value)
                       for suit in self.SUITS
                       for rank, value in self.VALUES.items() ]

    
    def deal_one(self):
        if not self.cards:
            self.reset()  
        index = random.randrange(len(self.cards))
        return self.cards.pop(index)
    
    def deal(self, n):
        return [self.deal_one() for _ in range(n)]
        
    def cards_left(self):
        return len(self.cards)

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

class Participant:
    def __init__(self, name):
        self.name = name
        self.hand = []  #list of (label, value) tuples

    def reset_hand(self):
        self.hand.clear()

    def receive(self, card):
        self.hand.append(card)

    def score(self):
        total = 0
        aces_as_elevens = 0
        for _, value in self.hand:
            total += value
            if value == 11:
                aces_as_elevens += 1

        while total > 21 and aces_as_elevens > 0:
            total -= 10
            aces_as_elevens -= 1
        
        return total
        

    def is_busted(self):
        return self.score() > 21

    def cards(self):
        return list(self.hand)

class Player(Participant):
    
    def __init__(self, name="You"): 
        super().__init__(name)

class Dealer(Participant):
    def __init__(self, name="Dealer"):
        super().__init__(name)
        self._hidden = True  # first card hidden during player turn

    def reset_hand(self):
        super().reset_hand()
        self._hidden = True

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
    
        return self.score() < 17

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
    # collect player labels
        player_labels = [label for (label, _) in self.player.cards()]
        player_total = self.player.score()  # call the method

    # collect dealer labels, handling "<hidden>" placeholder
        dealer_labels = []
        for c in self.dealer.visible_cards():
            if isinstance(c, tuple):
                dealer_labels.append(c[0])  # take the label
            else:
                dealer_labels.append(c)     # "<hidden>"

        print(f"Player: {', '.join(player_labels)} (total: {player_total})")
        print(f"Dealer: {', '.join(dealer_labels)}")

    def prompt_hit_or_stay(self) -> str:
        while True:
            choice = input("Hit or stay? [h/s]: ").strip().lower()
            if choice in ('h', 'hit'):
                return 'hit'
            if choice in ('s', 'stay'):
                return 'stay'
            print("Please enter 'h' (hit) or 's' (stay).")

    def player_turn(self):
        
        while True:
            choice = self.prompt_hit_or_stay()
            if choice == 'hit':
                self.player.receive(self.deck.deal_one())
                self.display_state(show_dealer_total = False)
                if self.player.is_busted():
                    break
            else: #the 'stay'
                break

    def dealer_turn(self):

        self.dealer.reveal_hidden()
        self.display_state(show_dealer_total=True)
        while self.dealer.should_hit():
            self.dealer.receive(self.deck.deal_one())
            self.display_state(show_dealer_total=True)

    def determine_result(self):
        
        if self.player.is_busted():
            return 'dealer'
        if self.dealer.is_busted():
            return 'player'

        p_total = self.player.score()
        d_total = self.dealer.score()

        if p_total > d_total:
            return 'player'
        if d_total > p_total:
            return 'dealer'
        return 'tie'

    def apply_bet(self, result):
        if result == 'player':
            self.bookie.win()
        elif result == 'dealer':
            self.bookie.lose()
        # tie: no change

    def ensure_deck_ready(self):
        if self.deck.cards_left() < 10: 
            self.deck.reset()

    # UI helpers
    def display_welcome_message(self): 
        print("Welcome to TwentyOne!")

    def display_goodbye_message(self): 
        print("Thanks for playing! Goodbye!")

    def _labels(self, cards_or_visible):
        labels = []
        for c in cards_or_visible:
            labels.append(c[0] if isinstance(c, tuple) else c)
        return ', '.join(labels)

    def display_state(self, show_dealer_total=False):
        p_labels = [lbl for (lbl, _) in self.player.cards()]
        p_total = self.player.score()

        if show_dealer_total:
            d_labels = [lbl for (lbl, _) in self.dealer.cards()]
            d_part = f"{', '.join(d_labels)} (total: {self.dealer.score()})"
        else:
            vis = self.dealer.visible_cards()
            d_labels = [(c[0] if isinstance(c, tuple) else c) for c in vis]
            d_part = ", ".join(d_labels)

        print(f"Player: {', '.join(p_labels)} (total: {p_total})")
        print(f"Dealer: {d_part}")

    def display_result(self, result):
        self.dealer.reveal_hidden()

        p_total = self.player.score()
        d_total = self.dealer.score()

        print("\nFinal hands:")
        print(f"Player: {self._labels(self.player.cards())} (total: {p_total})")
        print(f"Dealer: {self._labels(self.dealer.cards())} (total: {d_total})")

        if result == 'player':
            print("You win!")
        elif result == 'dealer':
            print("Dealer wins.")
        else:
            print("It's a tie.")

    def display_bank(self): 
        print(f"Bank: ${self.bookie.balance}")

    def play_again(self) -> bool:
        while True:
            choice = input("Play again? [y/n]: ").strip().lower()
            if choice in ('y', 'yes'):
                return True
            if choice in ('n', 'no'):
                return False
            print("Please enter 'y' or 'n'.")

if __name__ == "__main__": 
    deck = Deck() 
    player = Player() 
    dealer = Dealer() 
    bookie = Bookie() 

game = TwentyOneGame(deck, player, dealer, bookie) 
game.start()