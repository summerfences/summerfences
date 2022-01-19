# declaring variable
num = 3
# prints type of variable, displays integer
print(type(num))

# auto makes variable a float with decimal
pi = 3.14
print(type(pi))

# Arithmetic Operators:
# Addition
print(3 + 2)
# Subtraction
print(3 - 2)
# Multiplication
print(3 * 2)
# Division (Python 2 truncates decimal)
print(3 / 2)
# Floor Division (truncated decimal)
print(3 // 2)
# Exponent
print(3 ** 2)
# Modulus (Remainder after division)
# mod2 is only ever 1 or 0
print(3 % 2)
print(4 % 2)
print(5 % 2)
# Parentheses can be used to alter order of operation
print(3 * (2 + 1))

# incrementing values
num += 1
print(num)
# also works with other operators
num *= 10
print(num)

# Absolute value
print(abs(-3))

# Round to nearest integer
# comma states how many digits to round to
print(round(4.56749, 3))

# Comparisons(Output 'True' or 'False'):
# Equal: 3 == 2
# Not Equal: 3 != 2
# Greater Than: 3 > 2
# Less Than: 3 < 2
# Greater or Equal: 3 >= 2
# Less or Equal: 3 <= 2

num1 = 3
num2 = 2.7
print('Num 1 is ', num1)
print('Num 2 is ', num2)
print('Is num 2 greater than num 1?')
print(num1 < num2)  # false

# Sometimes strings can look like numbers
number = '100'
number_2 = '200'

# adds strings together, does NOT do arithmetic
print(number + number_2)  # 100200

# casting from string to integer
number = int(number)
number_2 = int(number_2)
print(number + number_2)  # 300
