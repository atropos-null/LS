import random
import numpy as np
from prettytable import PrettyTable

playing_cards = [
    ['Ace of Hearts'],
    ['Two of Hearts'],
    ['Three of Hearts'],
    ['Four of Hearts'],
    ['Five of Hearts'],
    ['Six of Hearts'],
    ['Seven of Hearts'],
    ['Eight of Hearts'],
    ['Nine of Hearts'],
    ['Ten of Hearts'],
    ['Jack of Hearts'],
    ['Queen of Hearts'],
    ['King of Hearts'],
    ['Ace of Diamonds'],
    ['Two of Diamonds'],
    ['Three of Diamonds'],
    ['Four of Diamonds'],
    ['Five of Diamonds'],
    ['Six of Diamonds'],
    ['Seven of Diamonds'],
    ['Eight of Diamonds'],
    ['Nine of Diamonds'],
    ['Ten of Diamonds'],
    ['Jack of Diamonds'],
    ['Queen of Diamonds'],
    ['King of Diamonds'],
    ['Ace of Clubs'],
    ['Two of Clubs'],
    ['Three of Clubs'],
    ['Four of Clubs'],
    ['Five of Clubs'],
    ['Six of Clubs'],
    ['Seven of Clubs'],
    ['Eight of Clubs'],
    ['Nine of Clubs'],
    ['Ten of Clubs'],
    ['Jack of Clubs'],
    ['Queen of Clubs'],
    ['King of Clubs'],
    ['Ace of Spades'],
    ['Two of Spades'],
    ['Three of Spades'],
    ['Four of Spades'],
    ['Five of Spades'],
    ['Six of Spades'],
    ['Seven of Spades'],
    ['Eight of Spades'],
    ['Nine of Spades'],
    ['Ten of Spades'],
    ['Jack of Spades'],
    ['Queen of Spades'],
    ['King of Spades']
    ]


tarot_fulldeck = [
    ['Ace of Cups'],
    ['Two of Cups'],
    ['Three of Cups'],
    ['Four of Cups'],
    ['Five of Cups'],
    ['Six of Cups'],
    ['Seven of Cups'],
    ['Eight of Cups'],
    ['Nine of Cups'],
    ['Ten of Cups'],
    ['Page of Cups'],
    ['Knight of Cups'],
    ['Queen of Cups'],
    ['King of Cups'],
    ['Ace of Coins'],
    ['Two of Coins'],
    ['Three of Coins'],
    ['Four of Coins'],
    ['Five of Coins'],
    ['Six of Coins'],
    ['Seven of Coins'],
    ['Eight of Coins'],
    ['Nine of Coins'],
    ['Ten of Coins'],
    ['Page of Coins'],
    ['Knight of Coins'],
    ['Queen of Coins'],
    ['King of Coins'],
    ['Ace of Clubs'],
    ['Two of Clubs'],
    ['Three of Clubs'],
    ['Four of Clubs'],
    ['Five of Clubs'],
    ['Six of Clubs'],
    ['Seven of Clubs'],
    ['Eight of Clubs'],
    ['Nine of Clubs'],
    ['Ten of Clubs'],
    ['Page of Clubs'],
    ['Knight of Clubs'],
    ['Queen of Clubs'],
    ['King of Clubs'],
    ['Ace of Swords'],
    ['Two of Swords'],
    ['Three of Swords'],
    ['Four of Swords'],
    ['Five of Swords'],
    ['Six of Swords'],
    ['Seven of Swords'],
    ['Eight of Swords'],
    ['Nine of Swords'],
    ['Ten of Swords'],
    ['Page of Swords'],
    ['Knight of Swords'],
    ['Queen of Swords'],
    ['King of Swords'],
    ['1 - Magician'],
    ['2 - Popess'],
    ['3 - Empress'],
    ['4 - Emperor'],
    ['5 - Pope'],
    ['6 - Lovers'],
    ['7 - Charioteer'],
    ['8 - Justice'],
    ['9 - Hermit'],
    ['10 - Wheel of Fortune'],
    ['11 - Strength'],
    ['12 - Hanged Man'],
    ['13 - Death'],
    ['14 - Temperance'],
    ['15 - Devil'],
    ['16 - Tower'],
    ['17 - Star'],
    ['18 - Moon'],
    ['19 - Sun'],
    ['20 - Judgement'],
    ['21 - The World'],
    ['0 - The Fool']
    ]

tarot_majors = [
     ['1 - Magician'],
    ['2 - Popess'],
    ['3 - Empress'],
    ['4 - Emperor'],
    ['5 - Pope'],
    ['6 - Lovers'],
    ['7 - Charioteer'],
    ['8 - Justice'],
    ['9 - Hermit'],
    ['10 - Wheel of Fortune'],
    ['11 - Strength'],
    ['12 - Hanged Man'],
    ['13 - Death'],
    ['14 - Temperance'],
    ['15 - Devil'],
    ['16 - Tower'],
    ['17 - Star'],
    ['18 - Moon'],
    ['19 - Sun'],
    ['20 - Judgement'],
    ['21 - The World'],
    ['0 - The Fool']
    ]


def main():
    headers = get_headers()
    deck = get_deck()
    spread = get_spread()
    random.shuffle(deck)
    the_pull = random.sample(deck, spread)
    array = np.array(the_pull)
    if spread == 3:
        reshaped_array = array.reshape((1, 3))
        table = PrettyTable(header=False)
        table.title = headers
        for row in reshaped_array:
            table.add_row(row)

    elif spread == 5:
        reshaped_array = array.reshape((1, 5))
        table = PrettyTable()
        table.title = headers
        table.field_names = ["Past", "Present", "Future", "Do", "Don't"]
        for row in reshaped_array:
            table.add_row(row)

    elif spread == 9:
        reshaped_array = array.reshape((3, 3))
        table = PrettyTable(header=False)
        table.title = headers
        for row in reshaped_array:
            table.add_row(row)

    print(table)


def get_headers():
    headers = input("What is your question? ").capitalize()
    return headers

def get_deck():
    """ chooses which list to draw from """
    deck = input("What deck do you want to use? Choose ‘playing cards’, ‘full deck’ or ‘majors’? ").lower()
    if deck == "playing cards":
        return playing_cards
    elif deck == "full deck":
        return tarot_fulldeck
    elif deck == "majors":
        return tarot_majors
    else:
        raise TypeError("Not a valid deck")

def get_spread():
    spread = input("What spread would you like? Choose '3', '5', or '9' ").lower()
    if spread == "3":
        return 3
    elif spread == "5":
        return 5
    elif spread == "9":
        return 9
    else:
        raise TypeError("Not a valid spread")


if __name__ == "__main__":
    main()


