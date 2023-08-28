import random

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

user_input = int(input(
    "What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. "))

computer_input = random.randint(0, 2)

if user_input == 0:
    user_input = rock

elif user_input == 1:
    user_input = paper

else:
    user_input = scissors


if computer_input == 0:
    computer_input = rock

elif computer_input == 1:
    computer_input = paper

else:
    computer_input = scissors


print(f'You chose {user_input}')
print(f'Computer chose {computer_input}')

if (user_input == computer_input):
    print("It's a raw!")

elif ((user_input == rock and computer_input == scissors)
      or (user_input == paper and computer_input == rock)
      or (user_input == scissors and computer_input == paper)):
    print('You win!')

else:
    print('You lose!')
