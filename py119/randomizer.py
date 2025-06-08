import random
from datetime import date
from collections import Counter

def main():

    user_choice = input("Welcome to Randomizer. 'selection' or 'stats': ")
    if user_choice == 'selection':
        selection()
    elif user_choice == 'stats':
        stats()
    else:
        print("Invalid choice. Please enter 'selection' or 'stats'.")

def selection():

    selection = []
    today = date.today()

    for _ in range (3):
        number = random.randint(1, 21)
        selection.append(number)

    with open("randomizer_log.txt", "a") as file:
        file.write(f"{today},{selection[0]},{selection[1]},{selection[2]}\n")

    print(f"Your problems for this round are: {', '.join(str(num) for num in selection)}.")

def stats():
    number_counts = Counter()
    total_rounds = 0
    try:
        with open("randomizer_log.txt", "r") as file:
            for line in file:
                parts = line.strip().split(",")
                if len(parts) == 4:
                    numbers = [int(n) for n in parts[1:]]
                    number_counts.update(numbers)
                    total_rounds += 1
    except FileNotFoundError:
        print("No log file found. Play at least one round first!")
        return

    print(f"\nStats:")
    print(f"Total rounds played: {total_rounds}")
    for n in range(1, 21):
        print(f"Number {n} was selected {number_counts[n]} times.")

if __name__ == "__main__":
    main()