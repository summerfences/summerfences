# Budgeting software by Frank Passantino, v1 8/21/21

# get user inputs
budget = input('Enter your monthly gross income: $')
rent = input('Enter your monthly rent cost: $')
util = input('Enter your monthly utilities cost: $')
gas = input('Enter your monthly gas cost: $')
groceries = input('Enter your monthly grocery cost: $')
entertain = input('Enter your monthly entertainment cost: $')
misc = input('Enter your monthly misc bills cost: $')

''' make calculations
this is done over two commands to break up the line '''
total_expenses = float(rent) + float(util) + float(gas) + float(misc)
total_expenses = total_expenses + float(groceries) + float(entertain)

# output info to user
print(f'Your total monthly gross income is ${budget}.')
print(f'Your total monthly expenses are ${total_expenses}.')

# if you made more than you spent
if float(budget) > float(total_expenses):
    net = float(budget) - float(total_expenses)
    print(f'You have a surplus of ${net}.')
# if you broke even for the month
elif float(budget) == float(total_expenses):
    print('Your gross income equals your expenses.')

# if you spent more than you made
elif float(budget) < float(total_expenses):
    over = float(total_expenses) - float(budget)
    print(f'You have a shortage of ${over}.')

# input validation
else:
    print('An error has occured. Please run the program again.')
