import random
import os


def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


def restart_game():
    if_user_want_restart = input(
        """If you want to start the game again, type 'yes'. 
If you want to stop the game, type 'no'. \n""")
    if if_user_want_restart == 'yes':
        cls()
        start_game()
    else:
        cls()


def start_game():
    print("""
         _____                       _______ _            _   _                 _               _ 
        / ____|                     |__   __| |          | \ | |               | |             | |
       | |  __ _   _  ___  ___ ___     | |  | |__   ___  |  \| |_   _ _ __ ___ | |__   ___ _ __| |
       | | |_ | | | |/ _ \/ __/ __|    | |  | '_ \ / _ \ | . ` | | | | '_ ` _ \| '_ \ / _ \ '__| |
       | |__| | |_| |  __/\__ \__ \    | |  | | | |  __/ | |\  | |_| | | | | | | |_) |  __/ |  |_|
        \_____|\__,_|\___||___/___/    |_|  |_| |_|\___| |_| \_|\__,_|_| |_| |_|_.__/ \___|_|  (_)""")

    print("""
Welcome to the Number Guessing Game!
I'm thinking of a number between 1 and 100""")

    random_number = random.randint(1, 100)
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard' : ")

    if (difficulty == 'easy'):
        remaining_attempts = 10
    else:
        remaining_attempts = 5

    while (remaining_attempts):
        print(
            f"You have {remaining_attempts} attempt(s) remaining to guess the number.")
        user_input = int(input("Make a guess : "))

        if (user_input > random_number):
            print('Too high')
            remaining_attempts -= 1

        elif (user_input < random_number):
            print('Too low')
            remaining_attempts -= 1
        else:
            print(f'You got it! The answer was {random_number}')
            restart_game()

    print("You've run out of guesses, you lose. ")
    restart_game()


start_game()
