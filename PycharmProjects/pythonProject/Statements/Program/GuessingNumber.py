from random import randint


def replay():
    return input('Do you want to play again? Enter Yes or No: ').lower().startswith('y')


lower_num = 1
higher_num = 50
randomNumber = randint(lower_num, higher_num)
numb_list = [1, 2, 3, 4, 5]
print(f"I'm thinking of a number between {lower_num} and {higher_num}.")
for number in numb_list:

    guess = int(input('What is your guess? '))

    if guess < lower_num or guess > higher_num:
        print('OUT OF BOUNDS! Please try again: ')
        continue

    elif randomNumber == guess:
        print(f'Congratulations! {randomNumber} You guessed the number.')
        print(f'CONGRATULATIONS, YOU GUESSED IT IN ONLY {number} GUESSES!!')
        break

    elif randomNumber > guess and number != numb_list:
        print(f"The number is greater than {guess}")

    elif randomNumber < guess and number != numb_list:
        print(f"The number is less than  {guess}")

    if number == len(numb_list):
        print(f"You have exhausted {number} trials.")
        print(f"The number was {randomNumber}")

    if not replay():
        break
