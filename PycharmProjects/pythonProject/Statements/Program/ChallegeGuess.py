from random import randint

num = randint(1, 100)
guesses = [0]

while True:

    guess = int(input("I'm thinking of a number between 1 and 100.\n  What is your guess? "))
    numb = 5
    if guess < 1 or guess > 100:
        print('OUT OF BOUNDS! Please try again: ')
        continue

    if guess == num:
        print(f'CONGRATULATIONS, YOU GUESSED IT IN ONLY {len(guesses)} GUESSES!!')
        break

    if len(guesses) == numb:
        print('your out of  chance')
        break
    guesses.append(guess)

    if guesses[-2]:
        if abs(num - guess) < abs(num - guesses[-2]):
            print('WARMER!')
        else:
            print('COLDER!')

    else:
        if abs(num - guess) <= 10:
            print('WARM!')
        else:
            print('COLD!')
