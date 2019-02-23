import random


def hang():
    gallows = [',--;-', '| ', '| ', '| ', '| ', '| ', '|_____']
    parts = iter([' 0 ', '/', '|', '\\', ' | ', ' A ', '/ ', '\\'])
    sequence = [1, 3, 1, 1, 2]
    for i, v in enumerate(sequence, start=1):
        for k in range(v):
            gallows[i] += next(parts)
            yield '/n'.join(gallows)
        raise StopIteration


def play():

        guess = input(f'Choose a letter!:')
        print(guess)
        with open('words.csv') as file:
            data = list(file)
            word_list = [data[:-1] for word in data if len(word) > 4]
            secret_word = random.choice(word_list)
            progress = ['_' for letter in secret_word]
        if guess in secret_word:
            for idx, letter in enumerate(secret_word):
                if letter == guess:
                    progress[idx] = guess
        else:
            return next(hang())

    # if all hangman parts are on the gallows:
    # print "Game over"
    # if all the letters were guessed correctly
    # print "Game over"
    # give the option to play again
    # if yes, return to screen
    # if no, break
