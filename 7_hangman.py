import random

word_list = ['cloud', 'rain', 'sun', 'moon', 'snow']

random_word_index = random.randint(0, len(word_list)-1)
random_word = word_list[random_word_index]

word_length = len(random_word)
user_life = len(random_word)

random_word_blank = []

for _ in range(word_length):
    random_word_blank += '_'

end_of_game = False

while (user_life > 0):
    if end_of_game == False:
        user_input = input('Please input the character\n')

        for i in range(word_length):
            letter = random_word[i]

            if letter == user_input:
                random_word_blank[i] = letter

        if user_input not in random_word:
            user_life -= 1
            print(
                f'You chose a wrong character, remaining life is {user_life}.\nThe Word : {random_word_blank}')
            if user_life == 0:
                print('Game over')
                end_of_game = True
        else:
            print(
                f'You chose a right character, remaining life is {user_life}.\nThe Word : {random_word_blank}')

if '_' not in random_word_blank:
    print('Game over')
    end_of_game = True
