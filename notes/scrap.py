def main():

    name = get_name_from_user()

    if name:
        print(f"Hi {name}")
    else:
        print("you must enter your name!")

def get_name_from_user():
    name = input("What is your name? ")
    return name

main()