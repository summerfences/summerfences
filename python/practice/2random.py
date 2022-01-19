# get random module 
import random as rnd

# declare and generate values
num1 = rnd.randint(1,100)
num2 = rnd.randint(1,100)

# Write the message in a variable and print
message = '''This program will generate two numbers.
It will then tell you if the two numbers match.
The first number is {}, and the second is {}.'''.format(num1, num2)
print(message)

if num1 == num2 :
    print('These numbers are a match!')


else :
    print('These numbers do not match.')

