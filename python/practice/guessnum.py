# guessing a random number

# import, declare, randomize
import random as rnd

number = rnd.randint(0, 10)

# prompt user
print('Enter a guess between 0-10: ')
guess = input()

# does not work?
if int(guess) == number:
    print('Correct! The number was ', number)

else:
    print('Incorrect. The number was ', number)
