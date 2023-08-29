import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
           'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

nr_list = [nr_letters, nr_symbols, nr_numbers]
total_nr = nr_letters + nr_symbols + nr_numbers
password = ''

while total_nr > 0:
    which_character = random.randint(0, 2)

    if nr_list[which_character] == 0:
        which_character = random.randint(0, 2)

    else:
        if which_character == 0:
            selected_letter = letters[random.randint(0, len(letters)-1)]
            password += selected_letter
            total_nr -= 1

        elif which_character == 1:
            selected_letter = str(numbers[random.randint(0, len(numbers)-1)])
            password += selected_letter
            total_nr -= 1

        else:
            selected_letter = symbols[random.randint(0, len(symbols)-1)]
            password += selected_letter
            total_nr -= 1

print(f'''Your password is
{password}''')
