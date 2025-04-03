username = input("What is your name? ").capitalize()


if "!" in username:
    uppername = username.upper()
    print(f"HELLO {uppername} WHY ARE WE YELLING?")
else:
    print(f"Hello {username}.")