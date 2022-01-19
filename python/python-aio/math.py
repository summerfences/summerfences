# import the math module
import math

# declare variables
pi = math.pi
e = math.e
tau = math.tau

# Display menu
print("""This program displays the values for pi, e, and tau.
1. pi
2. e
3. tau""")

# Get user choice
menu = input('Enter your selection: ')

# Display number based on selection
if int(menu) == 1:  # must convert input to integer
    print('The value of pi is', format(pi))
elif int(menu) == 2:
    print('The value of e is', format(e))
elif int(menu) == 3:
    print('The value of tau is', format(tau))
else:
    print('Invalid input')
