from random import shuffle

mylist = [' ', 'O', ' ']


def shuffle_list(my_list):
    shuffle(my_list)
    return my_list


def player_guess():
    guess = ''

    while guess not in ['0', '1', '2']:
        guess = input("Pick a number: 0, 1, or 2:  ")
    return int(guess)


def check_guess(my_list, guess):
    if mylist[guess] == 'O':
        print('Correct Guess!')
    else:
        print('Wrong! Better luck next time')
        print(mylist)


mixedup_list = shuffle_list(mylist)

guesses = player_guess()

check_guess(mixedup_list, guesses)
